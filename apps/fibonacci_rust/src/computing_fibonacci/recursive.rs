


pub fn fibonacci(number: i32) -> u64 {
	if number <= 0 {
		panic!("The number should be a non-null positive integer");
	}
	match number {
		1 | 2 => 1,
		_     => fibonacci(number - 1) + fibonacci(number - 2)
	}
}
