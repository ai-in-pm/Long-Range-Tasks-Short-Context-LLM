import json
import numpy as np
from time import time
from typing import Dict, List, Any
import os
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()

# Configure OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

class PRISM:
    def __init__(self, memory_capacity: int = 1000, model: str = "gpt-4"):
        """
        Initialize the PRISM system with a specified memory capacity.

        Args:
        memory_capacity (int): The maximum number of chunks to store in memory. Defaults to 1000.
        model (str): The OpenAI model to use. Defaults to "gpt-4".
        """
        self.memory = {}
        self.memory_capacity = memory_capacity
        self.model = model
        self.performance_metrics = {
            'processing_time': [],
            'memory_usage': [],
            'chunk_sizes': [],
            'token_usage': []
        }

    def get_completion(self, prompt: str) -> str:
        """Get completion from OpenAI API."""
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150,
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"Error in OpenAI API call: {e}")
            return ""

    def summarize(self, text: str) -> str:
        """
        Generate a concise summary of the input text using OpenAI API.

        Args:
        text (str): The text to be summarized.

        Returns:
        str: A summary of the input text.
        """
        prompt = f"Please provide a two-sentence summary of the following text:\n\n{text}"
        summary = self.get_completion(prompt)
        return summary if summary else "Summary generation failed."

    def update_memory(self, chunk: Dict[str, Any]) -> None:
        """
        Update the structured memory with new information.

        Args:
        chunk (Dict[str, Any]): A dictionary containing the text to be processed.
        """
        start_time = time()
        
        # Update memory while maintaining capacity
        if len(self.memory) >= self.memory_capacity:
            oldest_key = next(iter(self.memory))
            del self.memory[oldest_key]
        
        # Generate summary using OpenAI
        summary = self.summarize(chunk['text'])
        
        # Add new chunk to memory
        chunk_id = f"chunk_{len(self.memory)}"
        self.memory[chunk_id] = {
            'content': chunk['text'],
            'summary': summary,
            'timestamp': time()
        }
        
        # Record performance metrics
        processing_time = time() - start_time
        self.performance_metrics['processing_time'].append(processing_time)
        self.performance_metrics['memory_usage'].append(len(self.memory))
        self.performance_metrics['chunk_sizes'].append(len(chunk['text']))

    def process_chunks(self, chunks: List[Dict[str, str]]) -> None:
        """
        Process a list of text chunks and update memory.

        Args:
        chunks (List[Dict[str, str]]): A list of dictionaries containing the text to be processed.
        """
        for chunk in chunks:
            self.update_memory(chunk)
            print(f"Processed chunk: {self.memory[f'chunk_{len(self.memory)-1}']['summary']}")

    def get_performance_metrics(self) -> Dict[str, float]:
        """
        Return performance metrics of the system.

        Returns:
        Dict[str, float]: A dictionary containing performance metrics.
        """
        metrics = {
            'avg_processing_time': np.mean(self.performance_metrics['processing_time']),
            'max_memory_usage': max(self.performance_metrics['memory_usage']),
            'avg_chunk_size': np.mean(self.performance_metrics['chunk_sizes'])
        }
        return metrics

# Example usage
if __name__ == '__main__':
    prism = PRISM(memory_capacity=5)
    example_chunks = [
        {'text': 'The sun rose over the horizon, casting golden rays across the landscape. Birds began their morning chorus. The air was crisp and clear.'},
        {'text': 'In the dense forest, ancient trees stood like silent guardians. Their branches swayed gently in the breeze. Leaves rustled softly.'},
        {'text': 'A clear stream meandered through the valley, its waters crystal clear. Fish darted beneath the surface. The water sparkled in the sunlight.'}
    ]
    
    # Process chunks
    prism.process_chunks(example_chunks)
    
    # Display performance metrics
    metrics = prism.get_performance_metrics()
    print("\nPerformance Metrics:")
    for metric, value in metrics.items():
        print(f"{metric}: {value:.4f}")
