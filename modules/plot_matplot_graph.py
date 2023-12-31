import warnings

import numpy as np
from matplotlib import pyplot as plt


def gen_graph_figure(graph_type):
    # ==========================
    # === グラフ領域作成関数 ===
    # ==========================
    # graph_type : グラフタイプ (0:時間領域波形&周波数特性 / 1:時間領域波形&スペクトログラム)

    if graph_type == 0:
        # =========================================
        # === 時間領域波形&周波数特性グラフ向け ===
        # =========================================
        # figureインスタンスの作成
        fig = plt.figure(figsize=[7, 7])

        # Axesインスタンスの作成
        sub_fig1 = fig.add_subplot(2, 1, 1)
        sub_fig2 = fig.add_subplot(2, 1, 2)
        sub_fig3 = 0  # 未使用変数の定義

        # 上下左右にグラフ目盛線を付与
        sub_fig1.yaxis.set_ticks_position('both')
        sub_fig1.xaxis.set_ticks_position('both')
        sub_fig2.yaxis.set_ticks_position('both')
        sub_fig2.xaxis.set_ticks_position('both')

    else:
        # ===============================================
        # === 時間領域波形&スペクトログラムグラフ向け ===
        # ===============================================
        # figureインスタンスの作成
        fig = plt.figure(figsize=[8, 10])

        # Axesインスタンスの作成
        # add_axesの引数パラメータは「left，bottom，width，height」
        axes_left_common = 0.12
        axes_height_spctrgrm = 0.4
        axes_height_wave = 0.15
        axes_height_f0 = 0.22
        axes_bottom_f0 = 0.07
        axes_bottom_spctrgrm = axes_bottom_f0 + axes_height_f0 + 0.06
        axes_bottom_wave = axes_bottom_spctrgrm + axes_height_spctrgrm + 0.06
        axes_width_spctrgrm = 0.89  # 時間領域波形とスペクトログラムの横軸メモリが合うように微調整
        axes_width_wave = 0.71  # 時間領域波形とスペクトログラムの横軸メモリが合うように微調整
        axes_width_f0 = axes_width_wave

        sub_fig1 = fig.add_axes(
            (
                axes_left_common,
                axes_bottom_wave,
                axes_width_wave,
                axes_height_wave
            )
        )
        sub_fig2 = fig.add_axes(
            (
                axes_left_common,
                axes_bottom_spctrgrm,
                axes_width_spctrgrm,
                axes_height_spctrgrm
            )
        )
        sub_fig3 = fig.add_axes(
            (
                axes_left_common,
                axes_bottom_f0,
                axes_width_f0,
                axes_height_f0
            )
        )

        # 上下左右にグラフ目盛線を付与
        sub_fig1.yaxis.set_ticks_position('both')
        sub_fig1.xaxis.set_ticks_position('both')
        sub_fig2.yaxis.set_ticks_position('both')
        sub_fig2.xaxis.set_ticks_position('both')
        sub_fig3.yaxis.set_ticks_position('both')
        sub_fig3.xaxis.set_ticks_position('both')

    # fig       : 生成したmatplotlib figureインスタンス
    # sub_fig1  : 生成したmatplotlib 第1のAxesインスタンス
    # sub_fig2  : 生成したmatplotlib 第2のAxesインスタンス
    # sub_fig3  : 生成したmatplotlib 第3のAxesインスタンス
    return fig, sub_fig1, sub_fig2, sub_fig3


def gen_graph_figure_for_realtime_spctrgrm(spctrgrm_mode):
    # ==========================================================
    # === グラフ領域作成関数(リアルタイムスペクトログラム用) ===
    # ==========================================================
    # spctrgrm_mode : スペクトログラムデータ算出モード

    # figureインスタンスの作成
    fig = plt.figure(figsize=[7, 7])

    # Axesインスタンスの作成
    # add_axesの引数パラメータは「left，bottom，width，height」
    spctrgrm_axes_left = 0.12
    f0_axes_left = spctrgrm_axes_left

    spctrgrm_axes_width = 0.70
    f0_axes_width = spctrgrm_axes_width

    spctrgrm_axes_height = 0.38
    f0_axes_height = spctrgrm_axes_height

    f0_axes_bottom = 0.11
    spctrgrm_axes_bottom = f0_axes_bottom + f0_axes_height + 0.1

    spctrgrm_fig = fig.add_axes(
        (
            spctrgrm_axes_left,
            spctrgrm_axes_bottom,
            spctrgrm_axes_width,
            spctrgrm_axes_height
        )
    )

    f0_fig = fig.add_axes(
        (
            f0_axes_left,
            f0_axes_bottom,
            f0_axes_width,
            f0_axes_height
        )
    )

    # 上下左右にグラフ目盛線を付与
    spctrgrm_fig.yaxis.set_ticks_position('both')
    spctrgrm_fig.xaxis.set_ticks_position('both')
    f0_fig.yaxis.set_ticks_position('both')
    f0_fig.xaxis.set_ticks_position('both')

    # カラーバー用Axesインスタンスの作成
    # add_axesの引数パラメータは「left，bottom，width，height」
    cbar_fig = fig.add_axes(
        (spctrgrm_axes_left + spctrgrm_axes_width + 0.035,
         spctrgrm_axes_bottom,
         0.03,
         spctrgrm_axes_height)
    )

    # スペクトログラム算出モードテキスト表示設定
    text_ypos = 0.01

    if spctrgrm_mode == 0:
        text_xpos = 0.3
        text_word = "scipy.signal.spectrogram Function Mode"
    else:
        text_xpos = 0.32
        text_word = "Full Scratch STFT Function Mode"

    fig.text(text_xpos, text_ypos, text_word)

    # fig           : 生成したmatplotlib figureインスタンス
    # spctrgrm_fig  : スペクトログラム向けmatplotlib Axesインスタンス
    # cbar_fig      : スペクトログラムカラーバー向けmatplotlib Axesインスタンス
    # f0_fig        : 基本周波数 時系列波形向けmatplotlib Axesインスタンス
    return fig, spctrgrm_fig, cbar_fig, f0_fig


def gen_graph_figure_for_cepstrum():
    # ==========================================
    # === グラフ領域作成関数(ケプストラム用) ===
    # ==========================================

    # figureインスタンスの作成
    fig = plt.figure(figsize=[10, 7])

    # Axesインスタンスの作成
    sub_fig1 = fig.add_subplot(2, 2, 1)
    sub_fig2 = fig.add_subplot(2, 2, 2)
    sub_fig3 = fig.add_subplot(2, 2, 3)
    sub_fig4 = fig.add_subplot(2, 2, 4)

    # 上下左右にグラフ目盛線を付与
    sub_fig1.yaxis.set_ticks_position('both')
    sub_fig1.xaxis.set_ticks_position('both')
    sub_fig2.yaxis.set_ticks_position('both')
    sub_fig2.xaxis.set_ticks_position('both')
    sub_fig3.yaxis.set_ticks_position('both')
    sub_fig3.xaxis.set_ticks_position('both')
    sub_fig4.yaxis.set_ticks_position('both')
    sub_fig4.xaxis.set_ticks_position('both')

    # fig       : 生成したmatplotlib figureインスタンス
    # sub_fig1  : 生成したmatplotlib 第1のAxesインスタンス
    # sub_fig2  : 生成したmatplotlib 第2のAxesインスタンス
    # sub_fig3  : 生成したmatplotlib 第3のAxesインスタンス
    # sub_fig4  : 生成したmatplotlib 第3のAxesインスタンス
    return fig, sub_fig1, sub_fig2, sub_fig3, sub_fig4


def plot_time_and_freq(
    fig,
    wave_fig,
    freq_fig,
    data_normalized,
    time_normalized,
    time_range,
    amp_normalized,
    freq_normalized,
    freq_range,
    dbref,
    A,
    selected_mode
):
    # ====================================================
    # === 時間領域波形 & 周波数特性 グラフプロット関数 ===
    # ====================================================
    # fig               : 生成したmatplotlib figureインスタンス
    # wave_fig          : 時間領域波形向けmatplotlib Axesインスタンス
    # freq_fig          : 周波数特性向けmatplotlib Axesインスタンス
    # data_normalized   : 時間領域 波形データ(正規化済)
    # time_normalized   : 時間領域 X軸向けデータ [s]
    # time_range        : 時間領域波形グラフ X軸表示レンジ [sample count]
    # amp_normalized    : 周波数特性 振幅データ(正規化済)
    # freq_normalized   : 周波数特性 X軸向けデータ [Hz]
    # freq_range        : 周波数特性グラフ X軸表示レンジ [Hz]
    # dbref             : デシベル基準値
    # A                 : 聴感補正(A特性)の有効(True)/無効(False)設定
    # selected_mode     : 動作モード (0:レコーディングモード / 1:リアルタイムモード)

    # フォントサイズ設定
    plt.rcParams['font.size'] = 10

    # 目盛内側化
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'

    # 時間領域波形 軸ラベル設定
    wave_fig.set_xlabel("Time [s]")
    wave_fig.set_ylabel("Amplitude")

    # 周波数特性 軸ラベル設定
    freq_fig.set_xlabel("Frequency [Hz]")
    if (dbref > 0) and not (A):
        freq_fig.set_ylabel("Amplitude [dB spl]")
    elif (dbref > 0) and (A):
        freq_fig.set_ylabel("Amplitude [dB spl(A)]")
    else:
        freq_fig.set_ylabel("Log Power Spectrum [dB FS]")

    # 時間領域波形 軸目盛り設定
    wave_fig.set_xlim(0, time_range)
    wave_fig.set_ylim(-1.1, 1.1)
    wave_fig.set_yticks([-1, -0.5, 0, 0.5, 1])

    # 周波数特性 軸目盛り設定
    freq_fig.set_xlim(0, freq_range)
    if (dbref > 0):
        freq_fig.set_ylim(-10, 90)  # -10[dB] 〜 90[dB]
        freq_fig.set_yticks(np.arange(0, 100, 20))  # 20[dB]刻み(範囲:0〜100[dB])
    else:
        freq_fig.set_ylim(-100, 0)  # -10[dB] 〜 90[dB]

    # plot.figure.tight_layout()実行時の「UserWarning: The figure layout has
    # changed to tight」Warning文の抑止
    warnings.simplefilter("ignore", UserWarning)

    # レイアウト設定
    fig.tight_layout()

    # 時間領域波形データプロット
    wave_fig.plot(
        time_normalized,
        data_normalized,
        label="Time Waveform",
        lw=1,
        color="blue")

    # 周波数特性データプロット
    freq_fig.plot(
        freq_normalized,
        amp_normalized,
        label="Spectrum",
        lw=1,
        color="dodgerblue")

    # グラフの凡例表示
    wave_fig.legend(loc="upper right", borderaxespad=1, fontsize=8)
    freq_fig.legend(loc="upper right", borderaxespad=1, fontsize=8)

    if selected_mode == 1:
        # リアルタイムモードの場合、matplotlibグラフを更新
        plt.pause(0.0001)

        wave_fig.cla()
        freq_fig.cla()


def plot_time_and_spectrogram(
    fig,
    wave_fig,
    spctrgrm_fig,
    cbar_fig,
    f0_fig,
    data_normalized,
    time_normalized,
    time_range,
    freq_spctrgrm,
    time_spctrgrm,
    spectrogram,
    freq_range,
    f0,
    time_f0,
    dbref,
    A,
    selected_mode,
    spctrgrm_mode
):
    # ==========================================================
    # === 時間領域波形 & スペクトログラム グラフプロット関数 ===
    # ==========================================================
    # fig               : 生成したmatplotlib figureインスタンス
    # wave_fig          : 時間領域波形向けmatplotlib Axesインスタンス
    # spctrgrm_fig      : スペクトログラム向けmatplotlib Axesインスタンス
    # cbar_fig          : スペクトログラム向けmatplotlib カラーバー用Axesインスタンス
    # f0_fig                    : 基本周波数 時系列波形向けmatplotlib Axesインスタンス
    # data_normalized   : 時間領域 波形データ(正規化済)
    # time_normalized   : 時間領域 X軸向けデータ [ms]
    # time_range        : 時間領域波形グラフ X軸表示レンジ [sample count]
    # freq_spctrgrm     : スペクトログラム y軸向けデータ[Hz]
    # time_spctrgrm     : スペクトログラム x軸向けデータ[s]
    # spectrogram       : スペクトログラム 振幅データ
    # freq_range        : スペクトログラムグラフ Y軸表示レンジ[Hz]
    # f0                        : 基本周波数 時系列データ 1次元配列
    # time_f0                   : 基本周波数 時系列データに対応した時間軸データ 1次元配列
    # dbref             : デシベル基準値
    # A                 : 聴感補正(A特性)の有効(True)/無効(False)設定
    # selected_mode     : 動作モード (0:レコーディングモード / 1:リアルタイムモード)
    # spctrgrm_mode     : スペクトログラムデータ算出モード
    #                     (0:scipy.signal.spectrogram()関数を使用 / 1:自作STFT関数を使用)

    # フォントサイズ設定
    plt.rcParams['font.size'] = 10

    if selected_mode == 0:
        # ==================================
        # === レコーディングモードの場合 ===
        # ==================================

        # 目盛内側化
        wave_fig.tick_params(axis="both", direction="in")
        f0_fig.tick_params(axis="both", direction="in")

        # 時間領域波形 軸ラベル設定
        wave_fig.set_xlabel("Time [s]")
        wave_fig.set_ylabel("Amplitude")

        # スペクトログラム 軸ラベル設定
        spctrgrm_fig.set_xlabel("Time [s]")
        spctrgrm_fig.set_ylabel("Frequency [Hz]")

        # 基本周波数 時系列データ 軸ラベル設定
        f0_fig.set_xlabel("Time [s]")
        f0_fig.set_ylabel("Frequency [Hz]")

        # 時間領域波形 軸目盛り設定
        wave_fig.set_xlim(0, time_range)
        wave_fig.set_ylim(-1, 1)
        wave_fig.set_yticks([-1, -0.5, 0, 0.5, 1])

        # スペクトログラム 軸目盛り設定
        spctrgrm_fig.set_xlim(0, time_range)
        spctrgrm_fig.set_ylim(0, freq_range)  # 0 ～ 2000[Hz]の範囲

        # 基本周波数 時系列データ 軸目盛り設定
        f0_fig.set_xlim(0, time_range)
        f0_fig.set_ylim(-20, 1000)  # -20[Hz] 〜 1000[Hz]
        f0_fig.set_yticks(np.arange(0, 1020, 100))  # 100[Hz]刻み(範囲:0〜1020[Hz])

        # スペクトログラム算出モードテキスト表示設定
        text_ypos = 0.01

        if spctrgrm_mode == 0:
            text_xpos = 0.3
            text_word = "scipy.signal.spectrogram Function Mode"
        else:
            text_xpos = 0.32
            text_word = "Full Scratch STFT Function Mode"

        fig.text(text_xpos, text_ypos, text_word)

        # plot.figure.tight_layout()実行時の「UserWarning: The figure layout has
        # changed to tight」Warning文の抑止
        warnings.simplefilter("ignore", UserWarning)

        # レイアウト設定
        fig.tight_layout()

        # 時間領域波形データプロット
        wave_fig.plot(
            time_normalized,
            data_normalized,
            label="Time Waveform",
            lw=1,
            color="blue"
        )

        # スペクトログラムデータ範囲指定
        if dbref > 0:
            # スペクトログラムデータがdB SPLの場合
            colorbar_min = 0    # カラーバー最小値[dB]
            colorvar_max = 90   # カラーバー最大値[dB]
        else:
            # スペクトログラムデータがdB FSの場合
            colorbar_min = -100     # カラーバー最小値[dB]
            colorvar_max = 0        # カラーバー最大値[dB]

        # スペクトログラムデータプロット
        spctrgrm_im = spctrgrm_fig.pcolormesh(
            time_spctrgrm,
            freq_spctrgrm,
            spectrogram,
            vmin=colorbar_min,
            vmax=colorvar_max,
            cmap="jet"
        )

        # カラーバー設定
        cbar = fig.colorbar(spctrgrm_im)

        if (dbref > 0) and not (A):
            cbar.set_label("Sound Pressure [dB spl]")
        elif (dbref > 0) and (A):
            cbar.set_label("Sound Pressure [dB spl(A)]")
        else:
            cbar.set_label("Log Power Spectrum [dB FS]")

        # 基本周波数データプロット
        f0_fig.plot(
            time_f0,
            f0,
            label="Fundamental Frequency",
            lw=3,
            color="forestgreen"
        )

        # グラフの凡例表示
        wave_fig.legend(loc="upper right", borderaxespad=1, fontsize=8)
        f0_fig.legend(loc="upper right", borderaxespad=1, fontsize=8)

    else:
        # ================================
        # === リアルタイムモードの場合 ===
        # ================================

        # 目盛内側化
        f0_fig.tick_params(axis="both", direction="in")

        # スペクトログラム 軸ラベル設定
        spctrgrm_fig.set_xlabel("Time [s]")
        spctrgrm_fig.set_ylabel("Frequency [Hz]")

        # 基本周波数 時系列データ 軸ラベル設定
        f0_fig.set_xlabel("Time [s]")
        f0_fig.set_ylabel("Frequency [Hz]")

        # スペクトログラム 軸目盛り設定
        spctrgrm_fig.set_xlim(0, time_range)
        spctrgrm_fig.set_ylim(0, freq_range)

        # 基本周波数 時系列データ 軸目盛り設定
        f0_fig.set_xlim(0, time_range)
        f0_fig.set_ylim(-20, 1000)  # -20[Hz] 〜 1000[Hz]
        f0_fig.set_yticks(np.arange(0, 1020, 100))  # 100[Hz]刻み(範囲:0〜1020[Hz])

        # plot.figure.tight_layout()実行時の「UserWarning: The figure layout has
        # changed to tight」Warning文の抑止
        warnings.simplefilter("ignore", UserWarning)

        # レイアウト設定
        fig.tight_layout()

        # スペクトログラムデータ範囲指定
        if dbref > 0:
            # スペクトログラムデータがdB SPLの場合
            colorbar_min = 0    # カラーバー最小値[dB]
            colorvar_max = 90   # カラーバー最大値[dB]
        else:
            # スペクトログラムデータがdB FSの場合
            colorbar_min = -100     # カラーバー最小値[dB]
            colorvar_max = 0        # カラーバー最大値[dB]

        # スペクトログラムデータプロット
        spctrgrm_im = spctrgrm_fig.pcolormesh(
            time_spctrgrm,
            freq_spctrgrm,
            spectrogram,
            vmin=colorbar_min,
            vmax=colorvar_max,
            cmap="jet"
        )

        # カラーバー設定
        cbar = plt.colorbar(spctrgrm_im, orientation='vertical', cax=cbar_fig)

        if (dbref > 0) and not (A):
            cbar.set_label("Sound Pressure [dB spl]")
        elif (dbref > 0) and (A):
            cbar.set_label("Sound Pressure [dB spl(A)]")
        else:
            cbar.set_label("Log Power Spectrum [dB FS]")

        # 基本周波数データプロット
        f0_fig.plot(
            time_f0,
            f0,
            label="Fundamental Frequency",
            lw=3,
            color="forestgreen"
        )

        # グラフの凡例表示
        f0_fig.legend(loc="upper right", borderaxespad=1, fontsize=8)

        # リアルタイムモードの場合、matplotlibグラフを更新
        plt.pause(0.0001)

        # プロットデータの重なりを防ぐためにプロットデータクリアを実施
        f0_fig.cla()


def plot_time_freq_quef(
    fig,
    wave_fig,
    freq_fig,
    f0_fig,
    ceps_fig,
    data_normalized,
    time_normalized,
    time_range,
    amp_normalized,
    amp_envelope_normalized,
    freq_normalized,
    freq_range,
    f0,
    time_f0,
    cepstrum_db,
    cepstrum_data_lpl,
    dbref,
    A,
    selected_mode
):
    # ======================================================
    # === 時間領域波形 & ケプストラム グラフプロット関数 ===
    # ======================================================
    # fig                       : 生成したmatplotlib figureインスタンス
    # wave_fig                  : 時間領域波形向けmatplotlib Axesインスタンス
    # freq_fig                  : 周波数特性向けmatplotlib Axesインスタンス
    # f0_fig                    : 基本周波数 時系列波形向けmatplotlib Axesインスタンス
    # ceps_fig                  : ケプストラム向けmatplotlib Axesインスタンス
    # data_normalized           : 時間領域 波形データ(正規化済)
    # time_normalized           : 時間領域 X軸向けデータ [s]
    # time_range                : 時間領域波形グラフ X軸表示レンジ [sample count]
    # amp_normalized            : 周波数特性 振幅データ(正規化済)
    # amp_envelope_normalized   : スペクトル包絡データ(正規化済)
    # freq_normalized           : 周波数特性 X軸向けデータ [Hz]
    # freq_range                : 周波数特性グラフ X軸表示レンジ [Hz]
    # f0                        : 基本周波数 時系列データ 1次元配列
    # time_f0                   : 基本周波数 時系列データに対応した時間軸データ 1次元配列
    # cepstrum_data             : ケプストラムデータ(対数値)[dB] 1次元配列
    # cepstrum_data_lpl         : LPL(=Low-Pass-Lifter)適用後 ケプストラムデータ(対数値)[dB] 1次元配列
    # dbref                     : デシベル基準値
    # A                         : 聴感補正(A特性)の有効(True)/無効(False)設定
    # selected_mode             : 動作モード (0:レコーディングモード / 1:リアルタイムモード)

    # フォントサイズ設定
    plt.rcParams['font.size'] = 10

    # 目盛内側化
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'

    # 時間領域波形 軸ラベル設定
    wave_fig.set_xlabel("Time [s]")
    wave_fig.set_ylabel("Amplitude")

    # 周波数特性 軸ラベル設定
    freq_fig.set_xlabel("Frequency [Hz]")
    if (dbref > 0) and not (A):
        freq_fig.set_ylabel("Amplitude [dB spl]")
    elif (dbref > 0) and (A):
        freq_fig.set_ylabel("Amplitude [dB spl(A)]")
    else:
        freq_fig.set_ylabel("Log Power Spectrum [dB FS]")

    # 基本周波数 時系列データ 軸ラベル設定
    f0_fig.set_xlabel("Time [s]")
    f0_fig.set_ylabel("Frequency [Hz]")

    # ケプストラム 軸ラベル設定
    ceps_fig.set_xlabel("Quefrency [s]")
    if (dbref > 0) and not (A):
        ceps_fig.set_ylabel("Amplitude [dB spl]")
    elif (dbref > 0) and (A):
        ceps_fig.set_ylabel("Amplitude [dB spl(A)]")
    else:
        ceps_fig.set_ylabel("Log Power Spectrum [dB FS]")

    # 時間領域波形 軸目盛り設定
    wave_fig.set_xlim(0, time_range)
    wave_fig.set_ylim(-1.1, 1.1)
    wave_fig.set_yticks([-1, -0.5, 0, 0.5, 1])

    # 周波数特性 軸目盛り設定
    freq_fig.set_xlim(0, freq_range)
    if (dbref > 0):
        freq_fig.set_ylim(-10, 90)  # -10[dB] 〜 90[dB]
        freq_fig.set_yticks(np.arange(0, 100, 20))  # 20[dB]刻み(範囲:0〜100[dB])
    else:
        freq_fig.set_ylim(-100, 0)  # -10[dB] 〜 90[dB]

    # 基本周波数 時系列データ 軸目盛り設定
    f0_fig.set_xlim(0, time_range)
    f0_fig.set_ylim(-20, 1000)  # -20[Hz] 〜 1000[Hz]
    f0_fig.set_yticks(np.arange(0, 1020, 100))  # 100[Hz]刻み(範囲:0〜1020[Hz])

    # ケプストラム 軸目盛り設定
    ceps_fig.set_xlim(0, 0.02)  # 0 ～ 20[ms] (低ケフレンシ/高ケフレンシの境界を表示)
    ceps_fig.set_xticks(np.arange(0, 0.025, 0.005))  # 5[ms]刻み(範囲:0〜25[ms])
    ceps_fig.set_ylim(-1.5, 4)  # -1.5[dB] 〜4[dB]
    ceps_fig.set_yticks(np.arange(-1, 5, 1))  # 1[dB]刻み(範囲:-1〜5[dB])

    # plot.figure.tight_layout()実行時の「UserWarning: The figure layout has
    # changed to tight」Warning文の抑止
    warnings.simplefilter("ignore", UserWarning)

    # レイアウト設定
    fig.tight_layout()

    # 時間領域波形データプロット
    wave_fig.plot(
        time_normalized,
        data_normalized,
        label="Time Waveform",
        lw=1,
        color="blue"
    )

    # 周波数特性データプロット
    freq_fig.plot(
        freq_normalized,
        amp_normalized,
        label="Spectrum",
        lw=1,
        color="dodgerblue"
    )

    # スペクトル包絡データプロット
    freq_fig.plot(
        freq_normalized,
        amp_envelope_normalized,
        label="Spectrum Envelope",
        lw=4
    )

    # 基本周波数データプロット
    f0_fig.plot(
        time_f0,
        f0,
        label="Fundamental Frequency",
        lw=3,
        color="forestgreen"
    )

    # ケプストラムデータプロット
    ceps_fig.plot(
        time_normalized,
        cepstrum_db,
        label="Cepstrum",
        lw=1,
        color="red"
    )

    ceps_fig.plot(
        time_normalized,
        cepstrum_data_lpl,
        label="Cepstrum(Low-Pass-Lifter)",
        lw=1,
        color="royalblue"
    )

    # グラフの凡例表示
    wave_fig.legend(loc="upper right", borderaxespad=1, fontsize=8)
    freq_fig.legend(loc="upper right", borderaxespad=1, fontsize=8)
    f0_fig.legend(loc="upper right", borderaxespad=1, fontsize=8)
    ceps_fig.legend(loc="upper right", borderaxespad=1, fontsize=8)

    if selected_mode == 1:
        # リアルタイムモードの場合、matplotlibグラフを更新
        # (当該、pause()メソッドにより、show()メソッド無しでも、matplotlibグラフウィンドウが開く形となる(開いてすぐ閉じるイメージ))
        plt.pause(0.0001)

        # プロットデータの重なりを防ぐためにプロットデータクリアを実施
        wave_fig.cla()
        freq_fig.cla()
        f0_fig.cla()
        ceps_fig.cla()


def plot_time_freq_melfreq(
    fig,
    wave_fig,
    freq_fig,
    f0_fig,
    melfilbank_fig,
    data_normalized,
    time_normalized,
    time_range,
    amp_normalized,
    amp_envelope_normalized,
    freq_normalized,
    freq_range,
    f0,
    time_f0,
    melscale_amp_normalized,
    melscale_freq_normalized,
    mel_filter_number,
    mel_filter_bank,
    mfcc_amp_normalized,
    mfcc_dim,
    dbref,
    A,
    selected_mode
):
    # ======================================================
    # === 時間領域波形 & ケプストラム グラフプロット関数 ===
    # ======================================================
    # fig                       : 生成したmatplotlib figureインスタンス
    # wave_fig                  : 時間領域波形向けmatplotlib Axesインスタンス
    # freq_fig                  : 周波数特性向けmatplotlib Axesインスタンス
    # f0_fig                    : 基本周波数 時系列波形向けmatplotlib Axesインスタンス
    # melfilbank_fig            : メルフィルタバンク伝達関数向けmatplotlib Axesインスタンス
    # data_normalized           : 時間領域 波形データ(正規化済)
    # time_normalized           : 時間領域 X軸向けデータ [s]
    # time_range                : 時間領域波形グラフ X軸表示レンジ [sample count]
    # amp_normalized            : 周波数特性 振幅データ(正規化済)
    # amp_envelope_normalized   : スペクトル包絡データ(正規化済)
    # freq_normalized           : 周波数特性 X軸向けデータ [Hz]
    # freq_range                : 周波数特性グラフ X軸表示レンジ [Hz]
    # f0                        : 基本周波数 時系列データ 1次元配列
    # time_f0                   : 基本周波数 時系列データに対応した時間軸データ 1次元配列
    # melscale_amp_normalized        : メルフィルタバンク適用によるスペクトル包絡データ振幅成分 1次元配列
    # melscale_freq_normalized       : メル周波数軸データ 1次元配列
    # mel_filter_number         : メルフィルタバンク フィルタ数
    # mel_filter_bank           : メルフィルタバンク伝達関数(周波数特性) 1次元配列
    # mfcc_amp_normalized       : MFCCスペクトル包絡データ振幅成分 1次元配列
    # mfcc_dim                  : メル周波数ケプストラム係数(MFCC) 次元数
    # dbref                     : デシベル基準値
    # A                         : 聴感補正(A特性)の有効(True)/無効(False)設定
    # selected_mode             : 動作モード (0:レコーディングモード / 1:リアルタイムモード)

    # フォントサイズ設定
    plt.rcParams['font.size'] = 10

    # 目盛内側化
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'

    # 時間領域波形 軸ラベル設定
    wave_fig.set_xlabel("Time [s]")
    wave_fig.set_ylabel("Amplitude")

    # 周波数特性 軸ラベル設定
    freq_fig.set_xlabel("Frequency [Hz]")
    if (dbref > 0) and not (A):
        freq_fig.set_ylabel("Amplitude [dB spl]")
    elif (dbref > 0) and (A):
        freq_fig.set_ylabel("Amplitude [dB spl(A)]")
    else:
        freq_fig.set_ylabel("Log Power Spectrum [dB FS]")

    # 基本周波数 時系列データ 軸ラベル設定
    f0_fig.set_xlabel("Time [s]")
    f0_fig.set_ylabel("Frequency [Hz]")

    # メルフィルタバンク伝達関数 軸ラベル設定
    melfilbank_fig.set_xlabel("Frequency [Hz]")

    # 時間領域波形 軸目盛り設定
    wave_fig.set_xlim(0, time_range)
    wave_fig.set_ylim(-1.1, 1.1)
    wave_fig.set_yticks([-1, -0.5, 0, 0.5, 1])

    # 周波数特性 軸目盛り設定
    freq_fig.set_xlim(0, freq_range)
    if (dbref > 0):
        freq_fig.set_ylim(-10, 90)  # -10[dB] 〜 90[dB]
        freq_fig.set_yticks(np.arange(0, 100, 20))  # 20[dB]刻み(範囲:0〜100[dB])
    else:
        freq_fig.set_ylim(-100, 0)  # -10[dB] 〜 90[dB]

    # 基本周波数 時系列データ 軸目盛り設定
    f0_fig.set_xlim(0, time_range)
    f0_fig.set_ylim(-20, 1000)  # -20[Hz] 〜 1000[Hz]
    f0_fig.set_yticks(np.arange(0, 1020, 100))  # 100[Hz]刻み(範囲:0〜1020[Hz])

    # メルフィルタバンク伝達関数 軸目盛り設定
    melfilbank_fig.set_xlim(0, freq_range)

    # plot.figure.tight_layout()実行時の「UserWarning: The figure layout has
    # changed to tight」Warning文の抑止
    warnings.simplefilter("ignore", UserWarning)

    # レイアウト設定
    fig.tight_layout()

    # 時間領域波形データプロット
    wave_fig.plot(
        time_normalized,
        data_normalized,
        label="Time Waveform",
        lw=1,
        color="blue"
    )

    # 周波数特性データプロット
    freq_fig.plot(
        freq_normalized,
        amp_normalized,
        label="Spectrum",
        lw=1,
        color="dodgerblue"
    )

    # スペクトル包絡データプロット
    freq_fig.plot(
        freq_normalized,
        amp_envelope_normalized,
        label="Spectrum Envelope",
        lw=3
    )

    # メルスケール(メル尺度)スペクトル包絡データプロット
    freq_fig.plot(
        melscale_freq_normalized,
        melscale_amp_normalized,
        label=f"Mel-Scale Spectrum Envelope (Mel-filter nums: {mel_filter_number})",
        lw=1,
        marker='.'
    )

    # メル周波数ケプストラム係数(MFCC)スペクトル包絡データプロット
    freq_fig.plot(
        melscale_freq_normalized,
        mfcc_amp_normalized,
        label=f"MFCC Spectrum Envelope (MFCC dimensions: {mfcc_dim})",
        lw=2,
        color="limegreen"
    )

    # 基本周波数データプロット
    f0_fig.plot(
        time_f0,
        f0,
        label="Fundamental Frequency",
        lw=3,
        color="forestgreen"
    )

    # メルフィルタバンク伝達関数データプロット
    for i in range(mel_filter_number):
        melfilbank_fig.plot(
            freq_normalized,
            mel_filter_bank[i],
        )
    melfilbank_fig.set_title(f"mel filter bank (num filters: {mel_filter_number})", x=0.65, y=0.85)

    # グラフの凡例表示
    wave_fig.legend(loc="upper right", borderaxespad=1, fontsize=8)
    freq_fig.legend(loc="upper right", borderaxespad=1, fontsize=8)
    f0_fig.legend(loc="upper right", borderaxespad=1, fontsize=8)

    if selected_mode == 1:
        # リアルタイムモードの場合、matplotlibグラフを更新
        # (当該、pause()メソッドにより、show()メソッド無しでも、matplotlibグラフウィンドウが開く形となる(開いてすぐ閉じるイメージ))
        plt.pause(0.0001)

        # プロットデータの重なりを防ぐためにプロットデータクリアを実施
        wave_fig.cla()
        freq_fig.cla()
        f0_fig.cla()
        melfilbank_fig.cla()
