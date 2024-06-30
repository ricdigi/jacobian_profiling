
# Jacobian Profiling

## Scope
This project is about a performance investigation on different possible Jacobian function implementations  in sympy. The ultimate goal is to implement one of these functions in the sympy library. This would be very useful when linearizing equations of motion in dynamic sytems.

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/ricdigi/jacobian_profiling.git
    cd jacobian_profiling
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
   
## Directory Structure

``` 
jacobian_profiling/
│
├── implementations/
│   ├── __init__.py
│   ├── forward_jacobian_ric.py     # @ricdigi's implementation
│   ├── forward_jacobian_sam.py     # @brocksam's implementation
│   ├── jacobian_classic.py         # Classic sympy jacobian
│   ├── jacobian_protosym.py        # protosym based jacobian
    └── jacobian_symengine.py       # symengine based jacobian   
│
├── tests/
│   ├── __init__.py                 
│   ├── test_implementations.py     # Test the output of the functions
│   ├── conftest.py                 # Configuration file for pytest
│ 
│   
├── profiling/
│   ├── __init__.py        # Initialization file for profiling package
│   ├── profiler.py        # Main profiling logic
│   ├── utils.py           # Utility functions for profiling
│   
│
├── data/
│   ├── results.json         # Database for storing profiling results
│   
│
├── requirements.txt       # List of dependencies
├── README.md              # Project documentation
└── main.py                # Main script to run profiling
```


## Usage

Run the main script to profile the implementations:
```sh
python main.py
```

Results will be stored in the `data` directory.