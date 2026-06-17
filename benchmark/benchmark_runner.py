
import json
import time


class BenchmarkRunner:

	def __init__(self):

		self.results = {}

	def start(self, name):

		self.results[name] = {
			"start": time.time()
		}

	def stop(self, name):

		self.results[name]["end"] = (
			time.time()
		)

		self.results[name]["latency"] = (
			self.results[name]["end"]
			-
			self.results[name]["start"]
		)

	def save(self):

		with open(
			"benchmark_results.json",
			"w"
		) as f:

			json.dump(
				self.results,
				f,
				indent=4
			)
