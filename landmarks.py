import pandas as pd
from pathlib import Path


def calculate(distance_file='data/caucasiano.csv'):
    distances = pd.read_csv(distance_file, index_col=0)
    distances = distances.to_dict()['distance']

    # calcula medidas
    x = dict()
    y = dict()

    nse = distances['ven'] - distances['vn']

    x['n'] = 0
    y['n'] = distances['vn']

    x['che'] = x['n'] - distances['chsto']
    y['che'] = y['n'] + distances['nsto'] - distances['lssto'] + distances['lssto']

    x['chd'] = x['n'] + distances['chsto']
    y['chd'] = y['n'] + distances['nsto'] - distances['lssto'] + distances['lssto']

    x['p1e'] = x['n'] - (distances['enen'] / 2)
    y['p1e'] = y['n']

    x['p2e'] = x['n'] - (distances['enen'] / 2) - (
                (distances['ftft'] - distances['exex']) / 2) - distances['exen']
    y['p2e'] = y['n']

    x['ose'] = (x['p1e'] + x['p2e']) / 2
    y['ose'] = y['n'] - (distances['gsn'] - distances['nsn'])

    y['osd'] = y['n'] - (distances['gsn'] - distances['nsn'])
    x['p1d'] = x['n'] + (distances['enen'] / 2)
    y['p1d'] = y['n']
    x['p2d'] = x['n'] + (distances['enen'] / 2) + (
                (distances['ftft'] - distances['exex']) / 2) + distances['exen']
    y['p2d'] = y['n']
    x['osd'] = (x['p1d'] + x['p2d']) / 2

    # olho esquerdo
    x['ene'] = x['n'] - (distances['enen'] / 2)
    y['ene'] = y['n'] + nse
    x['exe'] = x['ene'] - distances['exen']
    y['exe'] = y['ene']
    x['pse'] = x['ene'] - (distances['exen'] / 2)
    y['pse'] = y['ene'] - (distances['pspi'] / 2)
    x['pie'] = x['ene'] - (distances['exen'] / 2)
    y['pie'] = y['ene'] + (distances['pspi'] / 2)

    # olho direito
    x['end'] = x['n'] + (distances['enen'] / 2)
    y['end'] = y['n'] + nse
    x['exd'] = x['end'] + distances['exen']
    y['exd'] = y['end']
    x['psd'] = x['end'] + (distances['exen'] / 2)
    y['psd'] = y['end'] - (distances['pspi'] / 2)
    x['pid'] = x['end'] + (distances['exen'] / 2)
    y['pid'] = y['end'] + (distances['pspi'] / 2)
    # nariz
    x['mfe'] = x['n'] - (distances['mfmf'] / 2)
    y['mfe'] = y['ene'] + 0.05 * distances['nsn']
    x['ale'] = x['n'] - (distances['alal'] / 2)
    y['ale'] = y['n'] + 0.85 * distances['nsn']
    x['ace'] = x['n'] - (distances['acac'] / 2)
    y['ace'] = y['n'] + distances['nsn']
    x['sn'] = x['n']
    y['sn'] = y['n'] + distances['nsn']

    x['mfd'] = x['n'] + (distances['mfmf'] / 2)
    y['mfd'] = y['ene'] + 0.05 * distances['nsn']
    x['ald'] = x['n'] + (distances['alal'] / 2)
    y['ald'] = y['n'] + 0.85 * distances['nsn']
    x['acd'] = x['n'] + (distances['acac'] / 2)
    y['acd'] = y['n'] + distances['nsn']

    # boca
    x['sto'] = x['li'] = x['ls'] = x['n']
    y['ls'] = y['n'] + distances['nsto'] - distances['lssto']
    y['li'] = y['ls'] + (2 * distances['lssto'])
    y['sto'] = y['ls'] + distances['lssto']

    # rugas olhos esquerdo
    x['p6e'] = x['exe'] - 2
    y['p6e'] = y['exe']
    x['p7e'] = x['p6e'] - 4
    y['p7e'] = y['p6e']
    x['p8e'] = x['p6e'] - 4
    y['p8e'] = y['p6e']

    x['p3e'] = x['p6e']
    y['p3e'] = y['p6e'] - 1.5
    x['p4e'] = x['p7e']
    y['p4e'] = y['p3e'] - 1.5
    x['p5e'] = x['p8e']
    y['p5e'] = y['p4e'] - 1.5

    x['p9e'] = x['p6e']
    y['p9e'] = y['p6e'] + 1.5
    x['p10e'] = x['p7e']
    y['p10e'] = y['p9e'] + 1.5
    x['p11e'] = x['p8e']
    y['p11e'] = y['p10e'] + 1.5

    # rugas olhos direito
    x['p6d'] = x['exd'] + 2
    y['p6d'] = y['exd']
    x['p7d'] = x['p6d'] + 4
    y['p7d'] = y['p6d']
    x['p8d'] = x['p6d'] + 4
    y['p8d'] = y['p6d']

    x['p3d'] = x['p6d']
    y['p3d'] = y['p6d'] - 1.5
    x['p4d'] = x['p7d']
    y['p4d'] = y['p3d'] - 1.5
    x['p5d'] = x['p8d']
    y['p5d'] = y['p4d'] - 1.5

    x['p9d'] = x['p6d']
    y['p9d'] = y['p6d'] + 1.5
    x['p10d'] = x['p7d']
    y['p10d'] = y['p9d'] + 1.5
    x['p11d'] = x['p8d']
    y['p11d'] = y['p10d'] + 1.5

    # palpebra inferior esquerda
    x['p12e'] = x['ene']
    y['p12e'] = (y['pie'] + 0.15 * distances['pior'])
    x['ore'] = x['p12e'] - (0.45 * distances['exen'])
    y['ore'] = y['pie'] + distances['pior']
    x['p13e'] = x['exe']
    y['p13e'] = (y['pie'] + 0.15 * distances['pior'])

    # palpebra inferior direita
    x['p12d'] = x['end']
    y['p12d'] = (y['pid'] + 0.15 * distances['pior'])
    x['ord'] = x['p12d'] + (0.45 * distances['exen'])
    y['ord'] = y['pid'] + distances['pior']
    x['p13d'] = x['exd']
    y['p13d'] = (y['pid'] + 0.15 * distances['pior'])

    # contorno esquerdo(rosto)
    x['sle'] = x['n']
    y['sle'] = y['sto'] + distances['stosl']
    x['tre'] = x['n']
    y['ve'] = y['n'] - distances['vn']
    y['tre'] = y['ve'] + distances['vtr']

    x['gne'] = x['n']
    y['gne'] = y['n'] + distances['ngn']
    x['goe'] = x['n'] - (distances['gogo'] / 2)
    y['goe'] = y['li'] + ((y['sle'] - y['li']) / 2)
    x['zye'] = x['n'] - (distances['zyzy'] / 2)
    y['zye'] = y['ore']
    x['te'] = x['n'] - (distances['tt'] / 2)
    y['te'] = y['pie'] + (distances['pior'] / 2)
    x['eue'] = x['n'] - (distances['eueu'] / 2)
    y['eue'] = y['tre']
    x['ve'] = x['n']
    y['ve'] = y['n'] - distances['vn']

    # contorno direito(rosto)
    x['vd'] = x['n']
    y['vd'] = y['n'] - distances['vn']

    x['sld'] = x['n']
    y['sld'] = y['sto'] + distances['stosl']
    x['trd'] = x['n']
    y['trd'] = y['vd'] + distances['vtr']
    x['v'] = 0
    y['v'] = 0

    x['gnd'] = x['n']
    y['gnd'] = y['n'] + distances['ngn']
    x['god'] = x['n'] + (distances['gogo'] / 2)
    y['god'] = y['li'] + ((y['sld'] - y['li']) / 2)
    x['zyd'] = x['n'] + (distances['zyzy'] / 2)
    y['zyd'] = y['ord']
    x['td'] = x['n'] + (distances['tt'] / 2)
    y['td'] = y['pid'] + (distances['pior'] / 2)
    x['eud'] = x['n'] + (distances['eueu'] / 2)
    y['eud'] = y['trd']

    # rugas testa cima
    x['fte'] = x['n'] - 0.5 * distances['ftft']
    y['fte'] = y['n'] - 0.5 * distances['trg']

    x['ftd'] = x['n'] + 0.5 * distances['ftft']
    y['ftd'] = y['n'] - 0.5 * distances['trg']

    x['pt3c'] = x['n']
    y['pt3c'] = y['tre'] + (0.5 * distances['trg'])
    x['pt1c'] = x['pt3c'] - (0.5 * distances['ftft'])
    y['pt1c'] = y['pt3c']
    x['pt2c'] = x['pt3c'] - (0.25 * distances['ftft'])
    y['pt2c'] = y['pt3c'] + (0.1 * distances['trg'])
    x['pt4c'] = x['pt3c'] + (0.25 * distances['ftft'])
    y['pt4c'] = y['pt3c'] + (0.1 * distances['trg'])
    x['pt5c'] = x['pt3c'] + (0.5 * distances['ftft'])
    y['pt5c'] = y['pt3c']

    # rugas testa meio
    x['pt3m'] = x['n']
    y['pt3m'] = y['tre'] + (0.35 * distances['trg'])
    x['pt1m'] = x['pt3m'] - (0.5 * distances['ftft'])
    y['pt1m'] = y['pt3m']
    x['pt2m'] = x['pt3m'] - (0.25 * distances['ftft'])
    y['pt2m'] = y['pt3m'] + (0.1 * distances['trg'])
    x['pt4m'] = x['pt3m'] + (0.25 * distances['ftft'])
    y['pt4m'] = y['pt3m'] + (0.1 * distances['trg'])
    x['pt5m'] = x['pt3m'] + (0.5 * distances['ftft'])
    y['pt5m'] = y['pt3m']

    # rugas testa baixo
    x['pt3b'] = x['n']
    y['pt3b'] = y['tre'] + (0.65 * distances['trg'])
    x['pt1b'] = x['pt3b'] - (0.5 * distances['ftft'])
    y['pt1b'] = y['pt3b']
    x['pt2b'] = x['pt3b'] - (0.25 * distances['ftft'])
    y['pt2b'] = y['pt3b'] + (0.1 * distances['trg'])
    x['pt4b'] = x['pt3b'] + (0.25 * distances['ftft'])
    y['pt4b'] = y['pt3b'] + (0.1 * distances['trg'])
    x['pt5b'] = x['pt3b'] + (0.5 * distances['ftft'])
    y['pt5b'] = y['pt3b']

    # pupilas
    x['se'] = x['n']
    y['se'] = y['ene']
    x['pupilae'] = x['se'] - distances['pupilse']
    y['pupilae'] = y['ore'] - distances['pupilor']
    x['pupilad'] = x['se'] + distances['pupilse']
    y['pupilad'] = y['ore'] - distances['pupilor']
    pupilaR = 0.6 * distances['pspi']

    # rugas sobrancelha
    x['pis1e'] = x['p1e'] + 0.84 * (x['n'] - x['p1e'])
    y['pis1e'] = y['n'] - 0.06 * nse
    x['pis2e'] = x['p1e'] + 0.87 * (x['n'] - x['p1e'])
    y['pis2e'] = y['n'] + 0.2 * nse
    x['pis3e'] = x['p1e'] + 0.62 * (x['n'] - x['p1e'])
    y['pis3e'] = y['n'] + 0.46 * nse

    x['pis1c'] = x['n']
    y['pis1c'] = y['pis1e']
    x['pis2c'] = x['n']
    x['pis3c'] = x['n']
    y['pis3c'] = y['pis3e']
    y['pis2c'] = y['pis3c'] - 0.5 * (y['pis3c'] - y['pis1c'])

    x['pis1d'] = x['p1d'] + 0.84 * (x['n'] - x['p1d'])
    y['pis1d'] = y['pis1e']
    x['pis2d'] = x['p1d'] + 0.87 * (x['n'] - x['p1d'])
    y['pis2d'] = y['pis2e']
    x['pis3d'] = x['p1d'] + 0.62 * (x['n'] - x['p1d'])
    y['pis3d'] = y['pis3e']

    # rugas nariz superior
    x['psn1c'] = x['mfe']
    y['psn1c'] = y['n'] + 0.25 * nse
    x['psn2c'] = x['n']
    y['psn2c'] = y['n'] + 0.05 * nse
    x['psn3c'] = x['mfd']
    y['psn3c'] = y['n'] + 0.25 * nse

    x['psn1m'] = x['mfe']
    y['psn1m'] = y['n'] + 0.5 * nse
    x['psn2m'] = x['n']
    y['psn2m'] = y['n'] + 0.6 * nse
    x['psn3m'] = x['mfd']
    y['psn3m'] = y['n'] + 0.5 * nse

    x['psn1b'] = x['mfe']
    y['psn1b'] = y['n'] + 0.75 * nse
    x['psn2b'] = x['n']
    y['psn2b'] = y['se']
    x['psn3b'] = x['mfd']
    y['psn3b'] = y['n'] + 0.75 * nse

    # rugas nariz inferior
    x['pn1e'] = x['ale'] + 0.22 * distances['alal']
    y['pn1e'] = y['n'] + 0.27 * distances['nsn']
    x['pn2e'] = x['ale'] + 0.24 * distances['alal']
    y['pn2e'] = y['n'] + 0.34 * distances['nsn']
    x['pn3e'] = x['ale'] + 0.4 * distances['alal']
    y['pn3e'] = y['n'] + 0.39 * distances['nsn']

    x['pn4e'] = x['ale'] + 0.2 * distances['alal']
    y['pn4e'] = y['n'] + 0.36 * distances['nsn']
    x['pn5e'] = x['ale'] + 0.26 * distances['alal']
    y['pn5e'] = y['n'] + 0.39 * distances['nsn']
    x['pn6e'] = x['ale'] + 0.28 * distances['alal']
    y['pn6e'] = y['n'] + 0.46 * distances['nsn']

    x['pn1d'] = x['ald'] - 0.22 * distances['alal']
    y['pn1d'] = y['n'] + 0.27 * distances['nsn']
    x['pn2d'] = x['ald'] - 0.24 * distances['alal']
    y['pn2d'] = y['n'] + 0.34 * distances['nsn']
    x['pn3d'] = x['ald'] - 0.4 * distances['alal']
    y['pn3d'] = y['n'] + 0.39 * distances['nsn']

    x['pn4d'] = x['ald'] - 0.2 * distances['alal']
    y['pn4d'] = y['n'] + 0.36 * distances['nsn']
    x['pn5d'] = x['ald'] - 0.26 * distances['alal']
    y['pn5d'] = y['n'] + 0.39 * distances['nsn']
    x['pn6d'] = x['ald'] - 0.28 * distances['alal']
    y['pn6d'] = y['n'] + 0.46 * distances['nsn']

    # rugas bochechas
    x['pb1e'] = x['ale'] + 0.1 * (x['ale'] - x['che'])
    y['pb1e'] = y['mfe'] + 0.6 * (y['sn'] - y['mfe'])
    x['pb2e'] = x['ale'] - 0.5 * (x['ale'] - x['che'])
    y['pb2e'] = y['pb1e'] + 0.15 * (y['che'] - y['pb1e'])
    x['pb3e'] = x['ale'] - 0.8 * (x['ale'] - x['che'])
    y['pb3e'] = y['pb1e'] + 0.35 * (y['che'] - y['pb1e'])
    x['pb4e'] = x['ale'] - 1.1 * (x['ale'] - x['che'])
    y['pb4e'] = y['pb1e'] + 0.55 * (y['che'] - y['pb1e'])
    x['pb5e'] = x['ale'] - 1.1 * (x['ale'] - x['che'])
    y['pb5e'] = y['pb1e'] + 0.8 * (y['che'] - y['pb1e'])

    x['pb1d'] = x['ald'] + 0.1 * (x['ald'] - x['chd'])
    y['pb1d'] = y['pb1e']
    x['pb2d'] = x['ald'] - 0.5 * (x['ald'] - x['chd'])
    y['pb2d'] = y['pb2e']
    x['pb3d'] = x['ald'] - 0.8 * (x['ald'] - x['chd'])
    y['pb3d'] = y['pb3e']
    x['pb4d'] = x['ald'] - 1.1 * (x['ald'] - x['chd'])
    y['pb4d'] = y['pb4e']
    x['pb5d'] = x['ald'] - 1.1 * (x['ald'] - x['chd'])
    y['pb5d'] = y['pb5e']

    # nazolabial
    x['pnl1e'] = x['ls'] - 0.83 * (x['ls'] - x['che'])
    y['pnl1e'] = y['ace']
    x['pnl3e'] = x['ls'] - 1.2 * (x['ls'] - x['che'])
    y['pnl3e'] = y['ls'] + 0.5 * (y['che'] - y['ls'])
    x['pnl2e'] = x['pnl3e'] - 0.1 * (x['pnl1e'] - x['pnl3e'])
    y['pnl2e'] = y['pnl1e'] + 0.61 * (y['pnl3e'] - y['pnl1e'])

    x['pnl1d'] = x['ls'] - 0.83 * (x['ls'] - x['chd'])
    y['pnl1d'] = y['acd']
    x['pnl3d'] = x['ls'] - 1.2 * (x['ls'] - x['chd'])
    y['pnl3d'] = y['ls'] + 0.5 * (y['che'] - y['ls'])
    x['pnl2d'] = x['pnl3d'] - 0.1 * (x['pnl1d'] - x['pnl3d'])
    y['pnl2d'] = y['pnl1d'] + 0.61 * (y['pnl3d'] - y['pnl1d'])

    # nazolabialInterna
    x['pnli1e'] = x['ls'] - 0.09 * (x['ls'] - x['che'])
    y['pnli1e'] = y['sn'] + 0.13 * (y['ls'] - y['sn'])
    x['pnli3e'] = x['ls'] - 0.16 * (x['ls'] - x['che'])
    y['pnli3e'] = y['sn'] + 0.8 * (y['ls'] - y['sn'])
    x['pnli2e'] = x['ls'] - 0.18 * (x['ls'] - x['che'])
    y['pnli2e'] = y['sn'] + 0.43 * (y['ls'] - y['sn'])

    x['pnli1d'] = x['ls'] - 0.09 * (x['ls'] - x['chd'])
    y['pnli1d'] = y['sn'] + 0.13 * (y['ls'] - y['sn'])
    x['pnli3d'] = x['ls'] - 0.16 * (x['ls'] - x['chd'])
    y['pnli3d'] = y['sn'] + 0.8 * (y['ls'] - y['sn'])
    x['pnli2d'] = x['ls'] - 0.18 * (x['ls'] - x['chd'])
    y['pnli2d'] = y['sn'] + 0.43 * (y['ls'] - y['sn'])

    landmarks = pd.DataFrame([x, y], index=['x', 'y'])
    file_name = Path(distance_file).stem
    landmarks.to_csv('data/landmarks_{}.csv'.format(file_name))
    landmarks.to_csv('data/landmarks.csv')
    return landmarks


if __name__ == '__main__':
    calculate()
