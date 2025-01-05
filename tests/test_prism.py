import unittest
from src.prism_agent import PRISM

class TestPRISM(unittest.TestCase):
    def setUp(self):
        self.prism = PRISM(memory_capacity=3)
        self.test_chunks = [
            {'text': 'First test chunk. Contains two sentences.'},
            {'text': 'Second test chunk. Another two sentences.'},
            {'text': 'Third test chunk. Final test sentences.'}
        ]

    def test_memory_capacity(self):
        """Test that memory capacity is respected"""
        # Process more chunks than capacity
        for chunk in self.test_chunks:
            self.prism.update_memory(chunk)
        
        self.assertEqual(len(self.prism.memory), 3)

    def test_summarization(self):
        """Test the summarization functionality"""
        text = "First sentence. Second sentence. Third sentence."
        summary = self.prism.summarize(text)
        self.assertEqual(summary, "First sentence. Second sentence.")

    def test_performance_metrics(self):
        """Test that performance metrics are being recorded"""
        for chunk in self.test_chunks:
            self.prism.update_memory(chunk)
        
        metrics = self.prism.get_performance_metrics()
        self.assertIn('avg_processing_time', metrics)
        self.assertIn('max_memory_usage', metrics)
        self.assertIn('avg_chunk_size', metrics)

    def test_update_memory(self):
        prism = PRISM()
        prism.update_memory({'key': 'value'})
        self.assertEqual(prism.memory['key'], 'value')

if __name__ == '__main__':
    unittest.main()
