Experiment(description='Repeat of 28th Aug experiment but deeper',
           data_dir='../data/tsdlr-250/',
           max_depth=12, 
           random_order=True,
           k=1,
           debug=False, 
           local_computation=False, 
           n_rand=9,
           sd=4, 
           max_jobs=400, 
           verbose=False,
           make_predictions=False,
           skip_complete=True,
           results_dir='../results/2013-09-03-time-series/',
           iters=150,
           base_kernels='StepTanh,BurstTanhSE,Per,Cos,Lin,SE,Const,MT5',
           zero_mean=True,
           random_seed=1,
           period_heuristic=5)
