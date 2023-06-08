use pyo3::prelude::pyfunction;


#[pyfunction]
pub fn fibonacci(number: i32) -> u64 {
	if number <= 0 {
		panic!("Please provide a positive integer starting with 1");
	}
	match number {
		1 | 2 => 1,
		_     => fibonacci(number - 1) + fibonacci(number - 2)
	}
}
