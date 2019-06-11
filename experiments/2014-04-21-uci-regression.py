Experiment(description='Multi d regression experiment',
           data_dir='../data/uci-regression',
           max_depth=20, 
           random_order=False,
           k=1,
           debug=False, 
           local_computation=False, 
           n_rand=9,
           sd=2, 
           jitter_sd=0.1,
           max_jobs=400, 
           verbose=False,
           make_predictions=False,
           skip_complete=True,
           results_dir='../results/2014-04-21-uci-regression/',
           iters=250,
           base_kernels='SE,Lin,Noise',
           random_seed=1,
           period_heuristic=3,
           max_period_heuristic=5,
           period_heuristic_type='min',
           subset=True,
           subset_size=250,
           full_iters=25,
           bundle_size=5,
           additive_form=True,
           mean='ff.MeanConst()',      # Starting mean
           kernel='ff.NoiseKernel()', # Starting kernel
           lik='ff.LikGauss(sf=-np.Inf)', # Starting likelihood 
           score='bic',
           stopping_criteria=['no_improvement'],
           improvement_tolerance=0.01,
           search_operators=[('A', ('+', 'A', 'B'), {'A': 'kernel', 'B': 'base'}),
                             ('A', ('*', 'A', 'B'), {'A': 'kernel', 'B': 'base-not-const'}),
                             ('A', ('*-const', 'A', 'B'), {'A': 'kernel', 'B': 'base-not-const'}),
                             ('A', 'B', {'A': 'kernel', 'B': 'base'}),
                             ('A', ('None',), {'A': 'kernel'})])