function sound_demo()
% A simple script to demonstrate the changepoint covariance.
%
% David Duvenaud
% Feb 2013

addpath(genpath(pwd))

n = 200;
D = 1;
x = linspace(-5, 5, n)';


%covfunc = {'covSum', {{'covProd',{'covRQiso','covChange'}}, {'covProd',{'covRQiso','covChange'}}}};
covfunc = {'covSum', {{'covProd',{'covPeriodic','covChange'}}, {'covProd',{'covPeriodic','covChange'}}}};
num_hypers = eval(feval(covfunc{:}));
hypers = randn(1, num_hypers)

K = feval( covfunc{:}, hypers, x, x);

%figure(1); clf; imagesc(K)
%title('Covariance matrix');

L = chol(K + eye(n).*max(K(:)).*1e-6);

y = L'*randn(n,1);
figure(2); clf; plot(x,y)
title('Random draw');

soundsc(y)

end

