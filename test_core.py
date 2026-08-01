import math
import app


def test_american_odds():
    assert math.isclose(app.american_implied_probability(-150), 0.6)
    assert math.isclose(app.american_implied_probability(150), 0.4)


def test_pair_normalization_and_cap():
    p = app.capped_pair_probability(-300, 250, 0.75)
    assert 0.5 <= p <= 0.75


def test_mlb_probability_cap():
    p = app.mlb_adjusted_top_probability(-500, 400, 0.75)
    assert 0.5 <= p <= 0.75


def test_wager_validation():
    assert app.valid_entry_value('.10')
    assert app.valid_entry_value('1.25')
    assert not app.valid_entry_value('1.234')
    assert not app.valid_entry_value('$1')


def test_secure_sequence_shape():
    seq = app.secure_sequence(50)
    assert len(seq) == 50
    assert set(seq) <= {1, 2}


def test_mac_framework_symbols_when_on_mac():
    if not app.IS_MAC:
        return
    assert app.Quartz is not None
    assert app.Vision is not None
    assert app.ApplicationServices is not None
    assert hasattr(app.Quartz, "CGPreflightScreenCaptureAccess")
    assert hasattr(app.Quartz, "CGRequestScreenCaptureAccess")
    assert hasattr(app.ApplicationServices, "AXIsProcessTrusted")
    assert hasattr(app.ApplicationServices, "AXIsProcessTrustedWithOptions")
    assert hasattr(app.ApplicationServices, "kAXTrustedCheckOptionPrompt")
