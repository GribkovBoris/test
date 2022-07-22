from test import visit_site_for_label


def test_visit():
    text = visit_site_for_label()
    print(text)
    assert text == "Your Store"


test_visit()
