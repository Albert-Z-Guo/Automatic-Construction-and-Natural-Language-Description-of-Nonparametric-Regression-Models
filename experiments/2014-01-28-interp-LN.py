Experiment(description='SE extrapolation experiment',
           data_dir='../data/tsdlr_5050/',
           max_depth=1, 
           random_order=False,
           k=1,
           debug=False, 
           local_computation=False, 
           n_rand=9,
           sd=2, 
           jitter_sd=0.1,
           max_jobs=1000, 
           verbose=False,
           make_predictions=True,
           skip_complete=True,
           results_dir='../results/2014-01-28-interp-LN/',
           iters=250,
           base_kernels='Lin',
           random_seed=1,
           subset=True,
           subset_size=250,
           full_iters=10,
           bundle_size=5,
           additive_form=True,
           mean='ff.MeanZero()',      # Starting mean
           kernel='ff.NoiseKernel() + ff.ConstKernel()', # Starting kernel
           lik='ff.LikGauss(sf=-np.Inf)', # Starting likelihood 
           score='bic',
           search_operators=[('A', ('+', 'A', 'B'), {'A': 'kernel', 'B': 'base'})])
