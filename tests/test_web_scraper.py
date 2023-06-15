import pytest
from web_scraper.scraper import (
    get_citations_needed_count,
    get_citations_needed_report
)

def test_get_citations_needed_count_wiki_try1():
    tst_url = "https://en.wikipedia.org/wiki/Numerical_control"
    actual = get_citations_needed_count(tst_url)
    expected = 2
    assert actual == expected

def test_get_citations_needed_count_wiki_try2():
    tst_url = "https://en.wikipedia.org/wiki/Water_jet_cutter"
    actual = get_citations_needed_count(tst_url)
    expected = 3
    assert actual == expected

def test_get_citations_needed_count_wiki_try3():
    tst_url = "https://en.wikipedia.org/wiki/Plasma_cutting"
    actual = get_citations_needed_count(tst_url)
    expected = 2
    assert actual == expected

def test_get_citations_needed_report_try1():
    tst_url = "https://en.wikipedia.org/wiki/Numerical_control"
    report = '\nThe high backlash mechanism itself is not necessarily relied on to be repeatedly precise for the cutting process, but some other reference object or precision surface may be used to zero the mechanism, by tightly applying pressure against the reference and setting that as the zero references for all following CNC-encoded motions. This is similar to the manual machine tool method of clamping a micrometer onto a reference beam and adjusting the Vernier dial to zero using that object as the reference.[citation needed]\n\n[Code Miscellaneous Functions (M-Code)][citation needed]. M-codes are miscellaneous machine commands that do not command axis motion. The format for an M-code is the letter M followed by two to three digits; for example:\n'
    actual = get_citations_needed_report(tst_url)
    expected = report
    assert actual == expected

def test_get_citations_needed_report_wiki_try2():
    tst_url = "https://en.wikipedia.org/wiki/Water_jet_cutter"
    actual = get_citations_needed_report(tst_url)
    expected = '\nThese advances in seal technology, plus the rise of plastics in the post-war years, led to the development of the first reliable high-pressure pump. The invention of Marlex by Robert Banks and John Paul Hogan of the Phillips Petroleum Company required a catalyst to be injected into the polyethylene.[17] McCartney Manufacturing Company in Baxter Springs, Kansas, began manufacturing these high-pressure pumps in 1960 for the polyethylene industry.[18] Flow Industries in Kent, Washington set the groundwork for commercial viability of waterjets with John Olsen’s development of the high-pressure fluid intensifier in 1973,[19] a design that was further refined in 1976.[20] Flow Industries then combined the high-pressure pump research with their waterjet nozzle research and brought waterjet cutting into the manufacturing world.[citation needed]\n\nMeatcutting using waterjet technology eliminates the risk of cross contamination since the contact medium is discarded.[citation needed]\n\nSpecially designed water jet cutters are commonly used to remove excess bitumen from road surfaces that have become the subject of binder flushing. Flushing is a natural occurrence caused during hot weather where the aggregate becomes level with the bituminous binder layer creating a hazardously smooth road surface during wet weather.[citation needed]\n'
    assert actual == expected

def test_get_citations_needed_report_wiki_try3():
    tst_url = "https://en.wikipedia.org/wiki/Plasma_cutting"
    actual = get_citations_needed_report(tst_url)
    expected = "\nProper eye protection and face shields are needed to prevent eye damage called arc eye as well as damage from debris. It is recommended to use green lens shade #5. OSHA recommends a shade 8 for arc current less than 300 A, but notes that \"These values apply where the actual arc is clearly seen. Experience has shown that lighter filters may be used when the arc is hidden by the workpiece.\"[4] Lincoln Electric, a manufacturer of plasma cutting equipment, says, \"Typically a darkness shade of #7 to #9 is acceptable.\" Longevity Global, Inc., another manufacturer, offers this more specific table for eye protection for plasma arc cutting at lower amperages:[citation needed]\n\nPlasma torches were once quite expensive. For this reason they were usually only found in professional welding shops and very well-stocked private garages and shops. However, modern plasma torches are becoming cheaper, and now are within the price range of many hobbyists, less than $300. Older units may be very heavy, but still portable, while some newer ones with inverter technology weigh only a little, yet equal or exceed the capacities of older ones.[citation needed]\n"
    assert actual == expected


