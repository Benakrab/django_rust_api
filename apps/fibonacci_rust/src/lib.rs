use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

mod computing_fibonacci;

use computing_fibonacci::recursive::__pyo3_get_function_fibonacci;


#[pymodule]
fn fibonacci_rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(fibonacci));
    Ok(())
}
