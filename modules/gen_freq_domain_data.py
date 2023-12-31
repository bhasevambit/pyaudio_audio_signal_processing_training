import numpy as np
import pyworld
import scipy

from .audio_signal_processing_basic import (a_weighting, db,
                                            dft_negative_freq_domain_exlusion,
                                            dft_normalize)


def gen_freq_domain_data(discrete_data, samplerate, dbref, A):
    # ================================
    # === 周波数特性データ生成関数 ===
    # ================================
    # discrete_data     : 時間領域波形 離散データ 1次元配列
    # samplerate        : サンプリング周波数[Hz]
    # dbref             : デシベル基準値
    # A                 : 聴感補正(A特性)の有効(True)/無効(False)設定

    # 時間領域波形 離散データ 1次元配列のDFT(離散フーリエ変換)を実施
    # (scipy.fft.fft()の出力結果spectrumは複素数)
    spectrum_data = scipy.fft.fft(discrete_data)

    # DFT(離散フーリエ変換)データに対応した周波数軸データを作成
    dt = 1 / samplerate  # サンプリング周期[s]
    freq_data = scipy.fft.fftfreq(len(discrete_data), d=dt)

    # DFT(離散フーリエ変換)データの正規化を実施
    # (振幅成分の正規化 & 負の周波数領域の除外)
    spectrum_normalized, amp_normalized, phase_normalized = dft_normalize(
        spectrum_data
    )

    # 周波数軸データの正規化(負の周波数領域の除外)を実施
    freq_normalized = dft_negative_freq_domain_exlusion(freq_data)

    # dbrefが0以上の場合、音圧レベル(dB SPL)に変換
    if dbref > 0:
        amp_normalized = db(amp_normalized, dbref)

        # dB変換されていてAがTrueの時に聴感補正する
        if A:
            amp_normalized += a_weighting(freq_normalized)
    else:
        # 正規化後 DFTデータ振幅成分を対数パワースペクトル(=10 * log10(amp^2))に変換
        amp_normalized = 20 * np.log10(amp_normalized)

    # spectrum_normalized   : 正規化後 DFTデータ 1次元配列
    # amp_normalized        : 正規化後 DFTデータ振幅成分 1次元配列
    # phase_normalized      : 正規化後 DFTデータ位相成分 1次元配列
    # freq_normalized       : 正規化後 周波数軸データ 1次元配列
    return spectrum_normalized, amp_normalized, phase_normalized, freq_normalized


def gen_freq_domain_data_of_signal_spctrgrm(
        data_normalized,
        samplerate,
        stft_frame_size,
        overlap_rate,
        window_func,
        dbref,
        A):
    # =============================================================
    # === 周波数特性データ生成関数 (scipy.signal.spectrogram版) ===
    # =============================================================
    # data_normalized       : 時間領域 波形データ(正規化済)
    # samplerate            : サンプリング周波数[Hz]
    # stft_frame_size       : STFT(短時間フーリエ変換)を行う時系列データ数(=STFTフレーム長)
    # overlap_rate          : オーバーラップ率 [%]
    # window_func           : 使用する窓関数
    # dbref                 : デシベル基準値
    # A                     : 聴感補正(A特性)の有効(True)/無効(False)設定

    freq_spctrgrm, time_spctrgrm, spectrogram = scipy.signal.spectrogram(
        # xは、「Time series of measurement values」
        # (= スペクトログラムデータの元となる時系列データ配列)
        x=data_normalized,
        # fsは、「Sampling frequency of the x time series」
        # (= サンプリング周波数)
        fs=samplerate,
        # windowは、使用する窓関数
        window=window_func,
        # npersegは、「Length of each segment」
        # (= STFT(短時間フーリエ変換)を行う時系列データ数(=STFTフレーム長))
        nperseg=stft_frame_size,
        # noverlapは、オーバラップするサンプリングデータ数を指定する
        # ([*] noverlapは、nperseg以下である必要あり)
        noverlap=(stft_frame_size * (overlap_rate / 100)),
        # nfftは、短時間FFTにおける周波数軸方向のデータ数を指定する
        # ([*] (設定値+1)/2 がスペクトログラムの周波数軸要素数となる)
        # ([*] nfftは、nperseg以上である必要あり)
        nfft=(stft_frame_size * 2) - 1,
        # scalingを"spectrum"を指定する事でスペクトログラムデータ単位が「2乗値」となるパワースペクトルとなる
        scaling="spectrum",
        # modeを"magnitude"とすることで、スペクトログラムデータとして振幅が算出される
        mode="magnitude"
    )

    print("freq_spctrgrm.shape = ", freq_spctrgrm.shape)
    print("time_spctrgrm.shape = ", time_spctrgrm.shape)
    print("spectrogram.shape [scipy org] = ", spectrogram.shape)

    # 聴感補正曲線を計算
    a_scale = a_weighting(freq_spctrgrm)
    print("a_scale.shape = ", a_scale.shape)

    # dbrefが0以上の場合、音圧レベル(dB SPL)に変換
    if dbref > 0:
        spectrogram = db(spectrogram, dbref)
        print("spectrogram.shape [dB SPL] = ", spectrogram.shape)

        # A=Trueの場合に、A特性補正を行う
        if A:
            for i in range(len(time_spctrgrm)):
                # 各時間軸データ(freq_spctrgrmと同じ次元サイズ)に対して、A特性補正を実施
                spectrogram[:, i] += a_scale

            print("spectrogram.shape [dB SPL(A)]= ", spectrogram.shape)
    else:
        # スペクトログラム 振幅データを対数パワースペクトル(=10 * log10(amp^2))に変換
        spectrogram = 20 * np.log10(spectrogram)
        print("spectrogram.shape [dB FS] = ", spectrogram.shape)

    print("")
    # freq_spctrgrm         : スペクトログラム y軸向けデータ[Hz]
    # time_spctrgrm         : スペクトログラム x軸向けデータ[s]
    # spectrogram           : スペクトログラム 振幅データ
    return freq_spctrgrm, time_spctrgrm, spectrogram


def gen_freq_domain_data_of_stft(
    time_array_after_window,
    samplerate,
    stft_frame_size,
    N_ave,
    final_time,
    acf,
    dbref,
    A
):
    # ===============================================================
    # === 周波数特性データ生成関数 (Full Scratch STFT Function版) ===
    # ===============================================================
    # time_array_after_window   : 時間領域 波形データ(正規化/オーバーラップ処理/hanning窓関数適用済)
    # samplerate                : サンプリング周波数[Hz]
    # stft_frame_size           : STFT(短時間フーリエ変換)を行う時系列データ数(=STFTフレーム長)
    # N_ave                     : オーバーラップ処理における切り出しフレーム数
    # final_time                : オーバーラップ処理で切り出したデータの最終時刻[s]
    # acf                       : 振幅補正係数(Amplitude Correction Factor)
    # dbref                     : デシベル基準値
    # A                         : 聴感補正(A特性)の有効(True)/無効(False)設定

    print("N_ave = ", N_ave)
    print("final_time = ", final_time)

    # スペクトログラムデータ格納配列の初期化
    spectrogram = []

    # DFT(離散フーリエ変換)データに対応した周波数軸データを作成
    dt = 1 / samplerate  # サンプリング周期[s]

    freq_data = scipy.fft.fftfreq(
        # nを、stft_frame_sizeの2倍とする事で、周波数分解能をscipy.signal.spectrogramと同じとする
        n=(stft_frame_size * 2),
        # dをサンプリング周期の2倍とする(scipy.signal.spectrogramと合わせる)
        d=dt
    )

    # 周波数軸データの正規化(負の周波数領域の除外)を実施
    freq_spctrgrm = dft_negative_freq_domain_exlusion(freq_data)
    print("freq_spctrgrm.shape = ", freq_spctrgrm.shape)

    # DFT(離散フーリエ変換)データに対応した時間軸データを作成
    # (開始:0 , 終了:オーバーラップ処理で切り出したデータの最終時刻[s],
    #  要素数:オーバーラップ処理における切り出しフレーム数)
    time_spctrgrm = np.linspace(0, final_time, N_ave)
    print("time_spctrgrm.shape = ", time_spctrgrm.shape)

    # 聴感補正曲線を計算
    a_scale = a_weighting(freq_spctrgrm)
    print("a_scale.shape = ", a_scale.shape)

    # 時間軸方向データ数分のループ処理
    for i in range(N_ave):

        # 時間領域 波形データのSTFTフレーム[i] に対して、フーリエ変換を実施
        # (scipy.fft.fft()の出力結果spectrumは複素数)
        spectrum_data = scipy.fft.fft(
            # xは「Input array, can be complex」
            x=time_array_after_window[i],
            # nは「Length of the transformed axis of the output」
            # (nを、stft_frame_sizeの2倍とする事で、周波数分解能をscipy.signal.spectrogramと同じとする)
            n=stft_frame_size * 2
        )

        # DFT(離散フーリエ変換)データの正規化を実施
        spectrum_normalized, amp_normalized, phase_normalized = dft_normalize(
            spectrum_data
        )

        # 窓関数補正値(acf)を乗算
        amp_normaliazed_acf = amp_normalized * acf

        # dbrefが0以上の場合、音圧レベル(dB SPL)に変換
        if dbref > 0:
            amp_normaliazed_acf = db(
                amp_normaliazed_acf, dbref
            )
        else:
            # DFT(離散フーリエ変換)データ 振幅成分を対数パワースペクトル(=10 * log10(amp^2))に変換
            amp_normaliazed_acf = 20 * np.log10(amp_normaliazed_acf)

        # spectrogram配列に追加
        spectrogram.append(amp_normaliazed_acf)

    # numpy.ndarray変換を行う
    spectrogram = np.array(spectrogram)
    print("spectrogram.shape = ", spectrogram.shape)

    # dbrefが0以上、かつ、A=Trueの場合に、A特性補正を行う
    if (dbref > 0) and A:
        spectrogram = spectrogram + a_scale
        print("spectrogram.shape [dB(A)] = ", spectrogram.shape)

    # 縦軸周波数、横軸時間にするためにデータを転置
    spectrogram = spectrogram.T
    print("spectrogram.shape [dB(A) and Transposed] = ", spectrogram.shape)

    print("")
    # freq_spctrgrm         : スペクトログラム y軸向けデータ[Hz]
    # time_spctrgrm         : スペクトログラム x軸向けデータ[s]
    # spectrogram           : スペクトログラム 振幅データ
    return freq_spctrgrm, time_spctrgrm, spectrogram


def gen_fundamental_freq_data(discrete_data, samplerate):
    # =======================================
    # === 基本周波数 時系列データ生成関数 ===
    # =======================================
    # discrete_data     : 時間領域波形 離散データ 1次元配列
    # samplerate        : サンプリング周波数[Hz]

    # === 基本周波数Rawデータの抽出

    # 基本周波数Rawデータ抽出における時間分解能 frame_period(ms単位)
    # (サンプリング周期の20倍の時間長とする)
    frame_period = (np.float64(1 / samplerate) * 1000) * 20

    f0_raw, time_f0 = pyworld.dio(x=discrete_data, fs=samplerate, frame_period=frame_period)
    # f0_raw    : 基本周波数 時系列データ 1次元配列(Rawデータ)
    # time_f0   : 基本周波数 時系列データに対応した時間軸データ 1次元配列

    # "StoneMask F0 refinement algorithm"を用いた基本周波数の補正(Refinement)
    f0 = pyworld.stonemask(x=discrete_data, f0=f0_raw, temporal_positions=time_f0, fs=samplerate)
    # f0        : 基本周波数 時系列データ 1次元配列

    # f0        : 基本周波数 時系列データ 1次元配列
    # time_f0   : 基本周波数 時系列データに対応した時間軸データ 1次元配列
    return f0, time_f0
