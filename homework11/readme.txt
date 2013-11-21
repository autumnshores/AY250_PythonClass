Homework 11

Bayes.ipynb contains code to estimate the full season batting average using bayesian statistics and MCMC, and answers questions a through e.


How I calculate alpha and beta for the Beta distribution prior for question b:

mean is defined as: 1/(1 + (beta/alpha)) = 0.255
variance is defined as: mean(1-mean)/(1+alpha+beta) = 0.0011
solve these two simultaneous equations to get alpha = 43.78, beta = 127.92 (to 2 d.p.).


Note: I tried looping over the players in one single model but the code didn't work in the end, so I created 13 separate models (sorry!!! i feel really bad about submitting super inelegant code, so you may dock a point for extreme inelegance :P I guess if I had started on this homework earlier I would have had more time to get the looping to work…). They can be found in batting_averagesX.py where X is the player number.