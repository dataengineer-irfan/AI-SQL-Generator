
import time

from benchmark.benchmark_runner import (
	BenchmarkRunner
)


def main():

	bench = BenchmarkRunner()

	bench.start(
		"generation"
	)

	time.sleep(1)

	bench.stop(
		"generation"
	)

	bench.save()

	print(
		"Benchmark Saved"
	)


if __name__ == "__main__":
	main()
