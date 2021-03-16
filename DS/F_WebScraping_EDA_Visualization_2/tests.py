from numpy.testing import assert_allclose
import matplotlib
matplotlib.use('Agg')
import pickle


class TestTop10CrypocurrenciesWithHigestMarketValueBarplot():

    @classmethod
    def setup_class(cls):
        cls.aplot = pickle.load(open('data/actual_plots/aplot1.pk', 'rb'))
        cls.gplot = pickle.load(open('plot1.pk', 'rb'))
        cls.apatches = cls.aplot.patches
        cls.gpatches = cls.gplot.patches


    def test_xticks(self):
        assert_allclose(self.aplot.get_xticks(),self.gplot.get_xticks(), rtol=1e-4)

    def test_yticks(self):
        assert_allclose(self.aplot.get_yticks(),self.gplot.get_yticks(), rtol=1e-4)

    def test_xticklabels(self):
        al = list(self.aplot.get_xticklabels())
        al = [ str(label) for label in al ]
        gl = list(self.gplot.get_xticklabels())
        gl = [ str(label) for label in gl ]
        assert al == gl

    def test_yticklabels(self):
        al = list(self.aplot.get_yticklabels())
        al = [ str(label) for label in al ]
        gl = list(self.gplot.get_yticklabels())
        gl = [ str(label) for label in gl ]
        assert al == gl

    def test_figwidth(self):
        assert self.aplot.figure.get_figwidth() == self.gplot.figure.get_figwidth()

    def test_figheight(self):
        assert self.aplot.figure.get_figheight() == self.gplot.figure.get_figheight()

    def test_xlabel(self):
        assert self.aplot.get_xlabel() == self.gplot.get_xlabel()

    def test_ylabel(self):
        assert self.aplot.get_ylabel() == self.gplot.get_ylabel()

    def test_title(self):
        assert self.aplot.get_title() == self.gplot.get_title()

    def test_patchcount(self):
        assert len(self.apatches) == len(self.gpatches)

    def test_bar1(self):
        assert_allclose(self.apatches[0].get_bbox().get_points(), self.gpatches[0].get_bbox().get_points(), rtol=1e-4)

    def test_bar2(self):
        assert_allclose(self.apatches[1].get_bbox().get_points(), self.gpatches[1].get_bbox().get_points(), rtol=1e-4)

    def test_bar3(self):
        assert_allclose(self.apatches[2].get_bbox().get_points(), self.gpatches[2].get_bbox().get_points(), rtol=1e-4)

    def test_bar4(self):
        assert_allclose(self.apatches[3].get_bbox().get_points(), self.gpatches[3].get_bbox().get_points(), rtol=1e-4)

    def test_bar5(self):
        assert_allclose(self.apatches[4].get_bbox().get_points(), self.gpatches[4].get_bbox().get_points(), rtol=1e-4)

    def test_bar6(self):
        assert_allclose(self.apatches[5].get_bbox().get_points(), self.gpatches[5].get_bbox().get_points(), rtol=1e-4)

    def test_bar7(self):
        assert_allclose(self.apatches[6].get_bbox().get_points(), self.gpatches[6].get_bbox().get_points(), rtol=1e-4)

    def test_bar8(self):
        assert_allclose(self.apatches[7].get_bbox().get_points(), self.gpatches[7].get_bbox().get_points(), rtol=1e-4)

    def test_bar9(self):
        assert_allclose(self.apatches[8].get_bbox().get_points(), self.gpatches[8].get_bbox().get_points(), rtol=1e-4)

    def test_bar10(self):
        assert_allclose(self.apatches[9].get_bbox().get_points(), self.gpatches[9].get_bbox().get_points(), rtol=1e-4)


class TestTrendOfPriceWithMarketValueScatterplot():

    @classmethod
    def setup_class(cls):
        cls.aplot = pickle.load(open('data/actual_plots/aplot2_axes.pk', 'rb'))
        cls.aplot_ax = cls.aplot[0][0]
        cls.gplot = pickle.load(open('plot2_axes.pk', 'rb'))
        cls.gplot_ax =  cls.gplot[0][0]
        cls.adata = pickle.load(open('data/actual_plots/aplot2_data.pk', 'rb'))
        cls.gdata = pickle.load(open('plot2_data.pk', 'rb'))


    def test_xticks(self):
        assert_allclose(self.aplot_ax.get_xticks(),self.gplot_ax.get_xticks(), rtol=1e-4)

    def test_yticks(self):
        assert_allclose(self.aplot_ax.get_yticks(),self.gplot_ax.get_yticks(), rtol=1e-4)

    def test_xticklabels(self):
        al = list(self.aplot_ax.get_xticklabels())
        al = [ str(label) for label in al ]
        gl = list(self.gplot_ax.get_xticklabels())
        gl = [ str(label) for label in gl ]
        assert al == gl

    def test_yticklabels(self):
        al = list(self.aplot_ax.get_yticklabels())
        al = [ str(label) for label in al ]
        gl = list(self.gplot_ax.get_yticklabels())
        gl = [ str(label) for label in gl ]
        assert al == gl

    def test_figwidth(self):
        assert self.aplot_ax.figure.get_figwidth() == self.gplot_ax.figure.get_figwidth()

    def test_figheight(self):
        assert self.aplot_ax.figure.get_figheight() == self.gplot_ax.figure.get_figheight()

    def test_xlabel(self):
        assert self.aplot_ax.get_xlabel() == self.gplot_ax.get_xlabel()

    def test_ylabel(self):
        assert self.aplot_ax.get_ylabel() == self.gplot_ax.get_ylabel()

    def test_title(self):
        assert self.aplot_ax.get_title() == self.gplot_ax.get_title()

    def test_datapoints(self):
        assert_allclose(self.adata.values, self.gdata.values, rtol=1e-4)

class TestTrendOfPriceWithVolumeScatterplot():

    @classmethod
    def setup_class(cls):
        cls.aplot = pickle.load(open('data/actual_plots/aplot3_axes.pk', 'rb'))
        cls.aplot_ax = cls.aplot[0][0]
        cls.gplot = pickle.load(open('plot3_axes.pk', 'rb'))
        cls.gplot_ax =  cls.gplot[0][0]
        cls.adata = pickle.load(open('data/actual_plots/aplot3_data.pk', 'rb'))
        cls.gdata = pickle.load(open('plot3_data.pk', 'rb'))


    def test_xticks(self):
        assert_allclose(self.aplot_ax.get_xticks(),self.gplot_ax.get_xticks(), rtol=1e-4)

    def test_yticks(self):
        assert_allclose(self.aplot_ax.get_yticks(),self.gplot_ax.get_yticks(), rtol=1e-4)

    def test_xticklabels(self):
        al = list(self.aplot_ax.get_xticklabels())
        al = [ str(label) for label in al ]
        gl = list(self.gplot_ax.get_xticklabels())
        gl = [ str(label) for label in gl ]
        assert al == gl

    def test_yticklabels(self):
        al = list(self.aplot_ax.get_yticklabels())
        al = [ str(label) for label in al ]
        gl = list(self.gplot_ax.get_yticklabels())
        gl = [ str(label) for label in gl ]
        assert al == gl

    def test_figwidth(self):
        assert self.aplot_ax.figure.get_figwidth() == self.gplot_ax.figure.get_figwidth()

    def test_figheight(self):
        assert self.aplot_ax.figure.get_figheight() == self.gplot_ax.figure.get_figheight()

    def test_xlabel(self):
        assert self.aplot_ax.get_xlabel() == self.gplot_ax.get_xlabel()

    def test_ylabel(self):
        assert self.aplot_ax.get_ylabel() == self.gplot_ax.get_ylabel()

    def test_title(self):
        assert self.aplot_ax.get_title() == self.gplot_ax.get_title()


    def test_datapoints(self):
        assert_allclose(self.adata.values, self.gdata.values, rtol=1e-4)


class TestTop10CrypocurrenciesWithHighestPositiveChangeBarplot():

    @classmethod
    def setup_class(cls):
        cls.aplot = pickle.load(open('data/actual_plots/aplot4.pk', 'rb'))
        cls.gplot = pickle.load(open('plot4.pk', 'rb'))
        cls.apatches = cls.aplot.patches
        cls.gpatches = cls.gplot.patches


    def test_xticks(self):
        assert_allclose(self.aplot.get_xticks(),self.gplot.get_xticks(), rtol=1e-4)

    def test_yticks(self):
        assert_allclose(self.aplot.get_yticks(),self.gplot.get_yticks(), rtol=1e-4)

    def test_xticklabels(self):
        al = list(self.aplot.get_xticklabels())
        al = [ str(label) for label in al ]
        gl = list(self.gplot.get_xticklabels())
        gl = [ str(label) for label in gl ]
        assert al == gl

    def test_yticklabels(self):
        al = list(self.aplot.get_yticklabels())
        al = [ str(label) for label in al ]
        gl = list(self.gplot.get_yticklabels())
        gl = [ str(label) for label in gl ]
        assert al == gl

    def test_figwidth(self):
        assert self.aplot.figure.get_figwidth() == self.gplot.figure.get_figwidth()

    def test_figheight(self):
        assert self.aplot.figure.get_figheight() == self.gplot.figure.get_figheight()

    def test_xlabel(self):
        assert self.aplot.get_xlabel() == self.gplot.get_xlabel()

    def test_ylabel(self):
        assert self.aplot.get_ylabel() == self.gplot.get_ylabel()

    def test_title(self):
        assert self.aplot.get_title() == self.gplot.get_title()

    def test_patchcount(self):
        assert len(self.apatches) == len(self.gpatches)

    def test_bar1(self):
        assert_allclose(self.apatches[0].get_bbox().get_points(), self.gpatches[0].get_bbox().get_points(), rtol=1e-4)

    def test_bar2(self):
        assert_allclose(self.apatches[1].get_bbox().get_points(), self.gpatches[1].get_bbox().get_points(), rtol=1e-4)

    def test_bar3(self):
        assert_allclose(self.apatches[2].get_bbox().get_points(), self.gpatches[2].get_bbox().get_points(), rtol=1e-4)

    def test_bar4(self):
        assert_allclose(self.apatches[3].get_bbox().get_points(), self.gpatches[3].get_bbox().get_points(), rtol=1e-4)

    def test_bar5(self):
        assert_allclose(self.apatches[4].get_bbox().get_points(), self.gpatches[4].get_bbox().get_points(), rtol=1e-4)

    def test_bar6(self):
        assert_allclose(self.apatches[5].get_bbox().get_points(), self.gpatches[5].get_bbox().get_points(), rtol=1e-4)

    def test_bar7(self):
        assert_allclose(self.apatches[6].get_bbox().get_points(), self.gpatches[6].get_bbox().get_points(), rtol=1e-4)

    def test_bar8(self):
        assert_allclose(self.apatches[7].get_bbox().get_points(), self.gpatches[7].get_bbox().get_points(), rtol=1e-4)

    def test_bar9(self):
        assert_allclose(self.apatches[8].get_bbox().get_points(), self.gpatches[8].get_bbox().get_points(), rtol=1e-4)

    def test_bar10(self):
        assert_allclose(self.apatches[9].get_bbox().get_points(), self.gpatches[9].get_bbox().get_points(), rtol=1e-4)

def main():
    a = TestTop10CrypocurrenciesWithHigestMarketValueBarplot()
    a.setup_class()
    a.test_xticks()




if __name__ == '__main__':
    main()


