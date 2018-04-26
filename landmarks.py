from pathlib import Path

import pandas as pd


def calculate(distance_file='data/caucasiano.csv'):
    distances = pd.read_csv(distance_file, index_col=0)
    distances = distances.to_dict()['distance']

    # calcula medidas
    z = dict()

    nse = distances['ven'] - distances['vn']

    z['n'] = (distances['ven'] / 2,
              distances['vn'])

    z['che'] = (z['n'][0] - distances['chsto'],
                z['n'][1] + distances['nsto'] - distances['lssto'] + distances['lssto'])

    z['chd'] = (z['n'][0] + distances['chsto'],
                z['n'][1] + distances['nsto'] - distances['lssto'] + distances['lssto'])

    z['p1e'] = (z['n'][0] - (distances['enen'] / 2), z['n'][1])

    z['p2e'] = (z['n'][0] - (distances['enen'] / 2) - ((distances['ftft'] - distances['exex']) / 2) - distances['exen'],
                z['n'][1])

    z['ose'] = ((z['p1e'][0] + z['p2e'][0]) / 2, z['n'][1] - (distances['gsn'] - distances['nsn']))

    add_interpolation(z, point_a='p1e', point_b='ose', name='pase1')
    add_interpolation(z, point_a='ose', point_b='p2e', name='pase2')

    z['p1d'] = (z['n'][0] + (distances['enen'] / 2),
                z['n'][1])

    z['p2d'] = ((z['n'][0] + (distances['enen'] / 2) + ((distances['ftft'] - distances['exex']) / 2) + distances[
        'exen']),
                z['n'][1])

    z['osd'] = ((z['p1d'][0] + z['p2d'][0]) / 2,
                z['n'][1] - (distances['gsn'] - distances['nsn']))

    add_interpolation(z, point_a='p1d', point_b='osd', name='pasd1')
    add_interpolation(z, point_a='osd', point_b='p2d', name='pasd2')

    # olho esquerdo
    z['ene'] = (z['n'][0] - (distances['enen'] / 2),
                z['n'][1] + nse)

    z['exe'] = (z['ene'][0] - distances['exen'],
                z['ene'][1])

    z['pse'] = (z['ene'][0] - (distances['exen'] / 2),
                z['ene'][1] - (distances['pspi'] / 2))

    z['pie'] = (z['ene'][0] - (distances['exen'] / 2),
                z['ene'][1] + (distances['pspi'] / 2))

    # olho direito
    z['end'] = (z['n'][0] + (distances['enen'] / 2),
                z['n'][1] + nse)

    z['exd'] = (z['end'][0] + distances['exen'],
                z['end'][1])

    z['psd'] = (z['end'][0] + (distances['exen'] / 2),
                z['end'][1] - (distances['pspi'] / 2))

    z['pid'] = (z['end'][0] + (distances['exen'] / 2),
                z['end'][1] + (distances['pspi'] / 2))

    # nariz
    z['mfe'] = (z['n'][0] - (distances['mfmf'] / 2),
                z['ene'][1] + 0.05 * distances['nsn'])

    z['ale'] = (z['n'][0] - (distances['alal'] / 2),
                z['n'][1] + 0.85 * distances['nsn'])

    z['ace'] = (z['n'][0] - (distances['acac'] / 2),
                z['n'][1] + distances['nsn'])

    z['sn'] = (z['n'][0],
               z['n'][1] + distances['nsn'])

    z['mfd'] = (z['n'][0] + (distances['mfmf'] / 2),
                z['ene'][1] + 0.05 * distances['nsn'])

    z['ald'] = (z['n'][0] + (distances['alal'] / 2),
                z['n'][1] + 0.85 * distances['nsn'])

    z['acd'] = (z['n'][0] + (distances['acac'] / 2),
                z['n'][1] + distances['nsn'])

    # boca
    z['ls'] = (z['n'][0],
               z['n'][1] + distances['nsto'] - distances['lssto'])

    z['sto'] = (z['n'][0],
                z['ls'][1] + distances['lssto'])

    z['li'] = (z['n'][0],
               z['ls'][1] + (2 * distances['lssto']))

    # rugas olhos esquerdo
    z['p6e'] = (z['exe'][0] - 2,
                z['exe'][1])

    z['p7e'] = (z['p6e'][0] - 4,
                z['p6e'][1])

    z['p8e'] = (z['p6e'][0] - 4,
                z['p6e'][1] - 1)

    z['p3e'] = (z['p6e'][0],
                z['p6e'][1] - 1.5)

    z['p4e'] = (z['p7e'][0],
                z['p3e'][1] - 1.5)

    z['p5e'] = (z['p8e'][0],
                z['p4e'][1] - 1.5)

    z['p9e'] = (z['p6e'][0],
                z['p6e'][1] + 1.5)

    z['p10e'] = (z['p7e'][0],
                 z['p9e'][1] + 1.5)

    z['p11e'] = (z['p8e'][0],
                 z['p10e'][1] + 1.5)

    # rugas olhos direito
    z['p6d'] = (z['exd'][0] + 2,
                z['exd'][1])

    z['p7d'] = (z['p6d'][0] + 4,
                z['p6d'][1])

    z['p8d'] = (z['p6d'][0] + 4,
                z['p6d'][1] - 1)

    z['p3d'] = (z['p6d'][0],
                z['p6d'][1] - 1.5)

    z['p4d'] = (z['p7d'][0],
                z['p3d'][1] - 1.5)

    z['p5d'] = (z['p8d'][0],
                z['p4d'][1] - 1.5)

    z['p9d'] = (z['p6d'][0],
                z['p6d'][1] + 1.5)

    z['p10d'] = (z['p7d'][0],
                 z['p9d'][1] + 1.5)

    z['p11d'] = (z['p8d'][0],
                 z['p10d'][1] + 1.5)

    # palpebra inferior esquerda
    z['p12e'] = (z['ene'][0],
                 (z['pie'][1] + 0.15 * distances['pior']))

    z['ore'] = (z['p12e'][0] - (0.45 * distances['exen']),
                z['pie'][1] + distances['pior'])

    z['p13e'] = (z['exe'][0],
                 (z['pie'][1] + 0.15 * distances['pior']))

    # palpebra inferior direita
    z['p12d'] = (z['end'][0],
                 (z['pid'][1] + 0.15 * distances['pior']))

    z['ord'] = (z['p12d'][0] + (0.45 * distances['exen']),
                z['pid'][1] + distances['pior'])

    z['p13d'] = (z['exd'][0],
                 (z['pid'][1] + 0.15 * distances['pior']))

    z['sle'] = (z['n'][0],
                z['sto'][1] + distances['stosl'])

    z['ve'] = (z['n'][0],
               z['n'][1] - distances['vn'])

    z['tre'] = (z['n'][0],
                z['ve'][1] + distances['vtr'])

    z['gne'] = (z['n'][0],
                z['n'][1] + distances['ngn'])

    z['goe'] = (z['n'][0] - (distances['gogo'] / 2),
                z['li'][1] + ((z['sle'][1] - z['li'][1]) / 2))

    # contorno esquerdo(rosto)
    z['zye'] = (z['n'][0] - (distances['zyzy'] / 2),
                z['ore'][1])

    z['te'] = (z['n'][0] - (distances['tt'] / 2),
               z['pie'][1] + (distances['pior'] / 2))

    z['eue'] = (z['n'][0] - (distances['eueu'] / 2),
                z['tre'][1])

    # contorno direito(rosto)
    z['vd'] = (z['n'][0],
               z['n'][1] - distances['vn'])

    z['sld'] = (z['n'][0],
                z['sto'][1] + distances['stosl'])

    z['trd'] = (z['n'][0],
                z['vd'][1] + distances['vtr'])

    z['v'] = (0, 0)
    z['v2'] = (z['v'][0], z['v'][1]-130)

    z['gnd'] = (z['n'][0],
                z['n'][1] + distances['ngn'])

    z['god'] = (z['n'][0] + (distances['gogo'] / 2),
                z['li'][1] + ((z['sld'][1] - z['li'][1]) / 2))

    z['zyd'] = (z['n'][0] + (distances['zyzy'] / 2),
                z['ord'][1])

    z['td'] = (z['n'][0] + (distances['tt'] / 2),
               z['pid'][1] + (distances['pior'] / 2))

    z['eud'] = (z['n'][0] + (distances['eueu'] / 2),
                z['trd'][1])

    # queixo
    z['ore_nge'] = (z['ore'][0],
                    z['gne'][1] - 10)
    z['gnd2'] = (z['gnd'][0],
                    z['gnd'][1] + 20)
    z['ord_ngd'] = (z['ord'][0],
                    z['gnd'][1] - 10)

    # rugas testa cima
    z['fte'] = (z['n'][0] - 0.5 * distances['ftft'],
                z['n'][1] - 0.5 * distances['trg'])

    z['ftd'] = (z['n'][0] + 0.5 * distances['ftft'],
                z['n'][1] - 0.5 * distances['trg'])

    z['pt3c'] = (z['n'][0],
                 z['tre'][1] + (0.5 * distances['trg']))

    z['pt1c'] = (z['pt3c'][0] - (0.5 * distances['ftft']),
                 z['pt3c'][1])

    z['pt2c'] = (z['pt3c'][0] - (0.25 * distances['ftft']),
                 z['pt3c'][1] + (0.1 * distances['trg']))

    z['pt4c'] = (z['pt3c'][0] + (0.25 * distances['ftft']),
                 z['pt3c'][1] + (0.1 * distances['trg']))

    z['pt5c'] = (z['pt3c'][0] + (0.5 * distances['ftft']),
                 z['pt3c'][1])

    # rugas testa meio
    z['pt3m'] = (z['n'][0],
                 z['tre'][1] + (0.35 * distances['trg']))

    z['pt1m'] = (z['pt3m'][0] - (0.5 * distances['ftft']),
                 z['pt3m'][1])

    z['pt2m'] = (z['pt3m'][0] - (0.25 * distances['ftft']),
                 z['pt3m'][1] + (0.1 * distances['trg']))

    z['pt4m'] = (z['pt3m'][0] + (0.25 * distances['ftft']),
                 z['pt3m'][1] + (0.1 * distances['trg']))

    z['pt5m'] = (z['pt3m'][0] + (0.5 * distances['ftft']),
                 z['pt3m'][1])

    # rugas testa baixo
    z['pt3b'] = (z['n'][0],
                 z['tre'][1] + (0.65 * distances['trg']))

    z['pt1b'] = (z['pt3b'][0] - (0.5 * distances['ftft']),
                 z['pt3b'][1])

    z['pt2b'] = (z['pt3b'][0] - (0.25 * distances['ftft']),
                 z['pt3b'][1] + (0.1 * distances['trg']))

    z['pt4b'] = (z['pt3b'][0] + (0.25 * distances['ftft']),
                 z['pt3b'][1] + (0.1 * distances['trg']))

    z['pt5b'] = (z['pt3b'][0] + (0.5 * distances['ftft']),
                 z['pt3b'][1])

    # pupilas
    z['se'] = (z['n'][0],
               z['ene'][1])

    z['pupilae'] = (z['se'][0] - distances['pupilse'],
                    z['ore'][1] - distances['pupilor'])

    z['pupilad'] = (z['se'][0] + distances['pupilse'],
                    z['ore'][1] - distances['pupilor'])

    pupilaR = 0.4 * distances['pspi']
    z['pupilaR'] = (pupilaR, pupilaR)

    # rugas sobrancelha
    z['pis1e'] = (z['p1e'][0] + 0.84 * (z['n'][0] - z['p1e'][0]),
                  z['n'][1] - 0.06 * nse)

    z['pis2e'] = (z['p1e'][0] + 0.87 * (z['n'][0] - z['p1e'][0]),
                  z['n'][1] + 0.2 * nse)

    z['pis3e'] = (z['p1e'][0] + 0.62 * (z['n'][0] - z['p1e'][0]),
                  z['n'][1] + 0.46 * nse)

    z['pis1c'] = (z['n'][0],
                  z['pis1e'][1])

    z['pis3c'] = (z['n'][0],
                  z['pis3e'][1])

    z['pis2c'] = (z['n'][0],
                  z['pis3c'][1] - 0.5 * (z['pis3c'][1] - z['pis1c'][1]))

    z['pis1d'] = (z['p1d'][0] + 0.84 * (z['n'][0] - z['p1d'][0]),
                  z['pis1e'][1])

    z['pis2d'] = (z['p1d'][0] + 0.87 * (z['n'][0] - z['p1d'][0]),
                  z['pis2e'][1])

    z['pis3d'] = (z['p1d'][0] + 0.62 * (z['n'][0] - z['p1d'][0]),
                  z['pis3e'][1])

    # rugas nariz superior
    z['psn1c'] = (z['mfe'][0],
                  z['n'][1] + 0.25 * nse)

    z['psn2c'] = (z['n'][0],
                  z['n'][1] + 0.05 * nse)

    z['psn3c'] = (z['mfd'][0],
                  z['n'][1] + 0.25 * nse)

    z['psn1m'] = (z['mfe'][0],
                  z['n'][1] + 0.5 * nse)

    z['psn2m'] = (z['n'][0],
                  z['n'][1] + 0.6 * nse)

    z['psn3m'] = (z['mfd'][0],
                  z['n'][1] + 0.5 * nse)

    z['psn1b'] = (z['mfe'][0],
                  z['n'][1] + 0.75 * nse)

    z['psn2b'] = (z['n'][0],
                  z['se'][1])

    z['psn3b'] = (z['mfd'][0],
                  z['n'][1] + 0.75 * nse)

    # rugas nariz inferior
    z['pn1e'] = (z['ale'][0] + 0.22 * distances['alal'],
                 z['n'][1] + 0.27 * distances['nsn'])

    z['pn2e'] = (z['ale'][0] + 0.24 * distances['alal'],
                 z['n'][1] + 0.34 * distances['nsn'])

    z['pn3e'] = (z['ale'][0] + 0.4 * distances['alal'],
                 z['n'][1] + 0.39 * distances['nsn'])

    z['pn4e'] = (z['ale'][0] + 0.2 * distances['alal'],
                 z['n'][1] + 0.36 * distances['nsn'])

    z['pn5e'] = (z['ale'][0] + 0.26 * distances['alal'],
                 z['n'][1] + 0.39 * distances['nsn'])

    z['pn6e'] = (z['ale'][0] + 0.28 * distances['alal'],
                 z['n'][1] + 0.46 * distances['nsn'])

    z['pn1d'] = (z['ald'][0] - 0.22 * distances['alal'],
                 z['n'][1] + 0.27 * distances['nsn'])

    z['pn2d'] = (z['ald'][0] - 0.24 * distances['alal'],
                 z['n'][1] + 0.34 * distances['nsn'])

    z['pn3d'] = (z['ald'][0] - 0.4 * distances['alal'],
                 z['n'][1] + 0.39 * distances['nsn'])

    z['pn4d'] = (z['ald'][0] - 0.2 * distances['alal'],
                 z['n'][1] + 0.36 * distances['nsn'])

    z['pn5d'] = (z['ald'][0] - 0.26 * distances['alal'],
                 z['n'][1] + 0.39 * distances['nsn'])

    z['pn6d'] = (z['ald'][0] - 0.28 * distances['alal'],
                 z['n'][1] + 0.46 * distances['nsn'])

    # rugas bochechas
    z['pb1e'] = (z['ale'][0] + 0.1 * (z['ale'][0] - z['che'][0]),

                 z['mfe'][1] + 0.6 * (z['sn'][1] - z['mfe'][1]))

    z['pb2e'] = (z['ale'][0] - 0.5 * (z['ale'][0] - z['che'][0]),

                 z['pb1e'][1] + 0.15 * (z['che'][1] - z['pb1e'][1]))

    z['pb3e'] = (z['ale'][0] - 0.8 * (z['ale'][0] - z['che'][0]),

                 z['pb1e'][1] + 0.35 * (z['che'][1] - z['pb1e'][1]))

    z['pb4e'] = (z['ale'][0] - 1.1 * (z['ale'][0] - z['che'][0]),

                 z['pb1e'][1] + 0.55 * (z['che'][1] - z['pb1e'][1]))

    z['pb5e'] = (z['ale'][0] - 1.1 * (z['ale'][0] - z['che'][0]),

                 z['pb1e'][1] + 0.8 * (z['che'][1] - z['pb1e'][1]))

    z['pb1d'] = (z['ald'][0] + 0.1 * (z['ald'][0] - z['chd'][0]),

                 z['pb1e'][1])

    z['pb2d'] = (z['ald'][0] - 0.5 * (z['ald'][0] - z['chd'][0]),

                 z['pb2e'][1])

    z['pb3d'] = (z['ald'][0] - 0.8 * (z['ald'][0] - z['chd'][0]),

                 z['pb3e'][1])

    z['pb4d'] = (z['ald'][0] - 1.1 * (z['ald'][0] - z['chd'][0]),

                 z['pb4e'][1])

    z['pb5d'] = (z['ald'][0] - 1.1 * (z['ald'][0] - z['chd'][0]),

                 z['pb5e'][1])

    # nazolabial
    z['pnl1e'] = (z['ls'][0] - 0.83 * (z['ls'][0] - z['che'][0]),

                  z['ace'][1])

    z['pnl3e'] = (z['ls'][0] - 1.2 * (z['ls'][0] - z['che'][0]),

                  z['ls'][1] + 0.5 * (z['che'][1] - z['ls'][1]))

    z['pnl2e'] = (z['pnl3e'][0] - 0.1 * (z['pnl1e'][0] - z['pnl3e'][0]),

                  z['pnl1e'][1] + 0.61 * (z['pnl3e'][1] - z['pnl1e'][1]))

    z['pnl1d'] = (z['ls'][0] - 0.83 * (z['ls'][0] - z['chd'][0]),

                  z['acd'][1])

    z['pnl3d'] = (z['ls'][0] - 1.2 * (z['ls'][0] - z['chd'][0]),

                  z['ls'][1] + 0.5 * (z['che'][1] - z['ls'][1]))

    z['pnl2d'] = (z['pnl3d'][0] - 0.1 * (z['pnl1d'][0] - z['pnl3d'][0]),

                  z['pnl1d'][1] + 0.61 * (z['pnl3d'][1] - z['pnl1d'][1]))

    # nazolabialInterna
    z['pnli1e'] = (z['ls'][0] - 0.09 * (z['ls'][0] - z['che'][0]),

                   z['sn'][1] + 0.13 * (z['ls'][1] - z['sn'][1]))

    z['pnli3e'] = (z['ls'][0] - 0.16 * (z['ls'][0] - z['che'][0]),

                   z['sn'][1] + 0.8 * (z['ls'][1] - z['sn'][1]))

    z['pnli2e'] = (z['ls'][0] - 0.18 * (z['ls'][0] - z['che'][0]),

                   z['sn'][1] + 0.43 * (z['ls'][1] - z['sn'][1]))

    z['pnli1d'] = (z['ls'][0] - 0.09 * (z['ls'][0] - z['chd'][0]),

                   z['sn'][1] + 0.13 * (z['ls'][1] - z['sn'][1]))
    z['pnli3d'] = (z['ls'][0] - 0.16 * (z['ls'][0] - z['chd'][0]),

                   z['sn'][1] + 0.8 * (z['ls'][1] - z['sn'][1]))

    z['pnli2d'] = (z['ls'][0] - 0.18 * (z['ls'][0] - z['chd'][0]),

                   z['sn'][1] + 0.43 * (z['ls'][1] - z['sn'][1]))

    file_name = Path(distance_file).stem
    landmarks = pd.DataFrame(z, index=('x', 'y'))
    landmarks.to_csv('data/landmarks_{}.csv'.format(file_name))
    landmarks.to_csv('data/landmarks.csv')
    return landmarks


def add_interpolation(arr, point_a, point_b, name=None):
    if name is None:
        name = 'i_{}_{}'.format(point_a, point_b)
    x = (arr[point_a][0] + arr[point_b][0]) / 2
    y = (arr[point_a][1] + arr[point_b][1]) / 2
    arr[name] = (x, y)


if __name__ == '__main__':
    calculate()
