import matplotlib.pyplot as plt
import time

class Grafico:
    def __init__(self, X, Y, T):
        self.x = X
        self.y = Y
        self.t = T
        self.Xatt = time.time()

        i = 0
        self.xt = []
        self.tt = []
        while i < len(X):
            self.xt.append(X[i])
            self.tt.append(T[i][:10])
            i += 24

        self.xt.append(X[-1])
        self.tt.append(T[-1][:10])

    def StampaGrafico(self):
        fig, ax = plt.subplots(figsize=(12,6))

        right_side = ax.spines["right"]
        right_side.set_visible(False)
        top_side = ax.spines["top"]
        top_side.set_visible(False)

        plt.plot(self.x, self.y, lw=1, c='red')
        plt.axvline(self.Xatt, c='red', lw=2)
        for xxt in self.xt:
            plt.axvline(xxt, c='blue', lw=1, ls='--')
        plt.xticks(self.xt, self.tt)
        plt.xlim(self.x[0], self.x[-1])
        # plt.savefig('test.png', transparent=True)
        return plt

class GraficoConPrecipitazioni(Grafico):
    def __init__(self, X, Y, T, Xprec, Yprec, Xcpr, Ycpr):
        super().__init__(X, Y, T)
        self.xprec = Xprec
        self.yprec = Yprec
        self.xcpr  = Xcpr
        self.ycpr  = Ycpr

    def StampaGraficoConPrec(self):
        fig, ax = plt.subplots(figsize=(12,6))

        right_side = ax.spines["right"]
        right_side.set_visible(False)
        top_side = ax.spines["top"]
        top_side.set_visible(False)
        ax.spines['bottom'].set_color('white')
        ax.spines['bottom'].set_linewidth(4)
        ax.spines['left'].set_color('white')
        ax.spines['left'].set_linewidth(4)
        ax.tick_params(axis='x', colors='white', labelsize= 18)
        ax.tick_params(axis='y', colors='white', labelsize= 18)

        plt.plot(self.x, self.y, lw=2, c='white')
        plt.plot(self.xprec, self.yprec, lw=3, ls=':', c='white')
        plt.plot(self.xcpr, self.ycpr, lw=1,ls='-.', c='white')

        plt.axvline(self.Xatt, c='lightblue', lw=2)
        for xxt in self.xt:
            plt.axvline(xxt, c='white', lw=1, ls='--')
        plt.xticks(self.xt, self.tt)
        plt.xlim(self.x[0], self.x[-1])

        return plt


if __name__ == '__main__':
    lati = 41.903
    longi = 12.48




