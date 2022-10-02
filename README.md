# Problem description (working on)
In this project the objective is finding the most effective factors among proposed on our data set (such as 'Eligiblity', 'Participant age', 'Participant gender' and etc) on 'quality score'. In fact, a questionnaire was designed by one the iranian medical researcher institue (Cohort) to collect data from their studied group. These questionnaires were filled via an interview and at the end of the interview, they considered a score to describe the quality of the collected data. They believe factors such as participants' education level, ehnicity, and things like these and also the interviewers' work experience, age and etc have effect on the qulity score of collected data but they do not know which factor or factors are most effective. Hence, we are going to invesigate this issue step by step, from early and simple data analysis methods such as visulization to advanced manners like desinging a Neural Network to find correlation. It is worth mentioning that this data set is accessable only via mailing me (m.mehdi_kr@outlook.com).

## Feature selection based on correlation matrix
At the first stage to achieve an intuition we used both Pearson and Spearman correlation to detect relationship between each factor and our target. The fundamental difference between the two correlation coefficients is that the Pearson coefficient works with a linear relationship between the two variables whereas the Spearman Coefficient works with monotonic relationships as well.This issue is explainable via below figures:



The results of applying these two correlation metrics were demonstrated below (respectively the first one is Pearson and the second one is Spearman correlation):


The thing about these metrics is that, they are not proper in nonlinear relation detection. Therefore, to detect any nonlinearity we have to employ stronger strategies. The below figure can make this issue more understanable:

## Feature selection based on visualization
Visualizing each pare of a factor and our target can make last step mateixes' vlues more sensable. Indeed, if you compare claculated correlation values between 'Month' and 'Quality Score' with their visualiztion, you can understand why both Pearson and Spearman correlation values of this pare is much more than other pares. 

From this step observtion it can be concluded the features can be classified into two main categories, numerical features (such as  'Interviewer_WorkExperience', 'Interviewer_age','FU_Month' ) and categorical features (such as 'Eligible', 'Participant_gender', 'Participant_ethnicity', 'Intervention_group', 'City_code', 'Village_Cluster', 'Village_StateCode','Interviewer_Gender','Interviewer_Education', 'Interviewer_Ethnicity'). So, it is much better to investigate each category seprately.

### Categorical features
The obtained results from correlation calculation illustrate that, the relationship (based on Pearson and Spearman) between each categorical feature and our target is too weak. The investigation of last step figures more precisely show that, this is because the variation of classes in each feature is almost the same. In fact, each classes' mean in each feature are really close to each other. So, a good strategy to improve the classes' variation of each categorical feature is combining them with each other. Indeed, the idea is combining small differences to make more sensable variations. As an example, combination of three features, which belong to interviewer ('Interviewer_Gender','Interviewer_Education', 'Interviewer_Ethnicity') is proposed in the below picture. Comparison between the combined features' figure and each feature's figure separately can show the created variaton perfectlty. 



At the first, I made my real effort to creat all the possible combination of these features. For example, all the possible way to opt two features from ten and combining them, all the possible way to opt three features from ten and combining them, all the possible way to opt four features from ten and combining them and etc. I did this strategy to combine two, three, four and five features and I found it is not an efficient way because not only take time to investigate all the combinations' figures, but also it is almost impposible beacuse the variation of many combinations are really close to each other.   

