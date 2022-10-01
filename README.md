# Problem description (working on)
In this project the objective is finding the most effective factors among proposed on our data set (such as 'Eligiblity', 'Participant age', 'Participant gender' and etc) on 'quality score'. In fact, a questionnaire was designed by one the iranian medical researcher institue (Cohort) to collect data from their studied group. These questionnaires were filled via an interview and at the end of the interview, they considered a score to describe the quality of the collected data. They believe factors such as participants' education level, ehnicity, and things like these and also the interviewers' work experience, age and etc have effect on the qulity score of collected data but they do not know which factor or factors are most effective. Hence, we are going to invesigate this issue step by step, from early and simple data analysis methods such as visulization to advanced manners like desinging a Neural Network to find correlation. It is worth mentioning that this data set is accessable only via mailing me (m.mehdi_kr@outlook.com).

## Feature selection based on correlation matrix
At the first stage to achieve an intuition we used both Pearson and Spearman correlation to detect relationship between each factor and our target. The fundamental difference between the two correlation coefficients is that the Pearson coefficient works with a linear relationship between the two variables whereas the Spearman Coefficient works with monotonic relationships as well.This issue is explainable via below figures:



The results of applying these two correlation metrics were demonstrated below (respectively the first one is Pearson and the second one is Spearman correlation):


The thing about these metrics is that, they are not proper in nonlinear relation detection. Therefore, to detect any nonlinearity we have to employ stronger strategies. The below figure can make this issue more understanable:

## Feature selection based on visualization
Visualizing each pare of a factor and our target can make last step mateixes' vlues more sensable. Indeed, if you compare claculated correlation values between 'Month' and 'Quality Score' with their visualiztion, you can understand why both Pearson and Spearman correlation values of this pare is much more than other pares. 

It is worth mentioning 

