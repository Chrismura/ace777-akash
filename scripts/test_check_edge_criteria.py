import unittest
from check_edge_criteria import evaluate, MIN_TRADES

T = lambda net, fee=0.5, reason="trailing_stop": {"net": net, "fee": fee, "reason": reason}


class TestEdgeCriteria(unittest.TestCase):
    def test_insufficient_data(self):
        verdict, d = evaluate([T(1.0)] * (MIN_TRADES - 1))
        self.assertEqual(verdict, "DONNEES_INSUFFISANTES")

    def test_edge_real(self):
        trades = [T(1.0, 0.3, "trailing_stop") for _ in range(30)]
        verdict, d = evaluate(trades)
        self.assertEqual(verdict, "EDGE_REEL")
        self.assertTrue(d["checks"]["c1_net_vs_frais"])
        self.assertTrue(d["checks"]["c2_winrate"])
        self.assertTrue(d["checks"]["c3_loss_concentration"])

    def test_fees_eat_margin(self):
        # net per trade 0.2 < fee per trade 0.5 → c1 fails
        trades = [T(0.2, 0.5) for _ in range(30)]
        verdict, d = evaluate(trades)
        self.assertEqual(verdict, "PAS_D_EDGE")
        self.assertFalse(d["checks"]["c1_net_vs_frais"])

    def test_low_winrate(self):
        trades = [T(1.0, 0.1)] * 10 + [T(-1.0, 0.1)] * 20
        verdict, d = evaluate(trades)
        self.assertEqual(verdict, "PAS_D_EDGE")
        self.assertFalse(d["checks"]["c2_winrate"])

    def test_loss_concentration(self):
        # 25 winners +5 losses all from stop_loss = 100% concentration
        trades = [T(2.0, 0.1, "trailing_stop") for _ in range(25)] + \
                 [T(-2.0, 0.1, "stop_loss") for _ in range(5)]
        verdict, d = evaluate(trades)
        self.assertEqual(verdict, "PAS_D_EDGE")
        self.assertFalse(d["checks"]["c3_loss_concentration"])

    def test_no_losses_passes_c3(self):
        trades = [T(1.0, 0.2, "trailing_stop") for _ in range(30)]
        verdict, _ = evaluate(trades)
        self.assertEqual(verdict, "EDGE_REEL")


if __name__ == "__main__":
    unittest.main()
