# Problem description (working on)
In this project the objective is finding the most effective factors among proposed on our data set (such as 'Eligiblity', 'Participant age', 'Participant gender' and etc) on 'quality score'. In fact, a questionnaire was designed by one the iranian medical researcher institue (Cohort) to collect data from their studied group. These questionnaires were filled via an interview and at the end of the interview, they considered a score to describe the quality of the collected data. They believe factors such as participants' education level, ehnicity, and things like these and also the interviewers' work experience, age and etc have effect on the qulity score of collected data but they do not know which factor or factors are most effective. Hence, we are going to invesigate this issue step by step, from early and simple data analysis methods such as visulization to advanced manners like desinging a Neural Network to find correlation. It is worth mentioning that this data set is accessable only via mailing me (m.mehdi_kr@outlook.com).

## Feature selection based on correlation matrix
At the first stage to achieve an intuition we used both Pearson and Spearman correlation to detect relationship between each factor and our target. The fundamental difference between the two correlation coefficients is that the Pearson coefficient works with a linear relationship between the two variables whereas the Spearman Coefficient works with monotonic relationships as well.This issue is explainable via below figures:


![State 1](https://user-images.githubusercontent.com/42337253/194723779-b66fbdff-edfd-461c-9ad0-497d9dd5df27.PNG)

![State 2](https://user-images.githubusercontent.com/42337253/194723785-310cafdb-6d46-4f3f-9764-9c4c0a216c49.PNG)

![State 3](https://user-images.githubusercontent.com/42337253/194723786-1494ceef-d8ee-47db-9993-4ca0384f2153.PNG)

![State 4](https://user-images.githubusercontent.com/42337253/194723790-d2afb1af-0eed-417a-9a67-93d2a0c06c8d.PNG)

![State 5](https://user-images.githubusercontent.com/42337253/194723793-3000a41c-b493-41fa-b219-63dbe4567d6a.PNG)




The results of applying these two correlation metrics were demonstrated below (respectively the first one is Pearson and the second one is Spearman correlation). This part code is uploaded as 'Correlation matrix':

![Pearson corr](https://user-images.githubusercontent.com/42337253/194738203-f29671be-c942-49e3-82af-345721f3bd28.PNG)

![Spearman corr](https://user-images.githubusercontent.com/42337253/194738207-4285717a-1a11-4803-abc0-55466b0c4bfc.PNG)


The thing about these metrics is that, they are not proper in nonlinear relation detection (The below figure can make this issue more understanable). Therefore, to detect any nonlinearity we have to employ stronger strategies. 

![State 6](https://user-images.githubusercontent.com/42337253/194723801-b2639a4a-dabc-4070-a85b-394585837a14.PNG)

## Feature selection based on visualization
Visualizing each pare of a factor and our target can make last step mateixes' vlues more sensable. Indeed, if you compare claculated correlation values between 'Month' and 'Quality Score' with their visualiztion, you can understand why both Pearson and Spearman correlation values of this pare is much more than other pares. This part script is uploaded as 'Visualization'.

![Eligible](https://user-images.githubusercontent.com/42337253/194738733-266cb4f1-2ff8-48b4-87ca-0c7e53d46ec1.png)

![Intervention group](https://user-images.githubusercontent.com/42337253/194738746-ddc59ccf-9c58-49fc-9db7-24c1a7724e5b.png)

![Interviewer Ethnicity](https://user-images.githubusercontent.com/42337253/194738751-42f73f0d-8a4f-413a-8108-41da8bb9ac94.png)

![Interviewer Gender](https://user-images.githubusercontent.com/42337253/194738758-07ef016d-22fe-4a6e-9931-4b71cba4770f.png)

![Participant ethnicity](https://user-images.githubusercontent.com/42337253/194738762-0bbb7ef2-e332-47b7-af6d-de5f67b947f5.png)

![Participant gender](https://user-images.githubusercontent.com/42337253/194738767-6bf64633-5b45-4fa4-adb9-c345c6a0039a.png)

![Village StateCode](https://user-images.githubusercontent.com/42337253/194738790-ed4e49f6-a3f8-4398-9f44-b44025de792e.png)

![Interviewer Education](https://user-images.githubusercontent.com/42337253/194738749-2f59852c-f78b-4494-852a-ad8fd23bb503.png)

![City code](https://user-images.githubusercontent.com/42337253/194739707-4c9df5ec-e450-41d7-8abb-79ec495a0072.png)

![Village Cluster](https://user-images.githubusercontent.com/42337253/194738775-3aadc8cc-f3d2-435c-a20d-c296822b28b4.png)

![Village Participant Nubmer](https://user-images.githubusercontent.com/42337253/194738784-3e7516e0-93be-4259-bfbd-e09d4c6bb9a6.png)

![Participant age](https://user-images.githubusercontent.com/42337253/194739576-5883177f-f0ac-4d13-a93f-11f2a846511a.png)

![Interviewer WorkExperience](https://user-images.githubusercontent.com/42337253/194739581-c26e7f04-76c1-41d6-88a4-a9872a36c67a.png)

![Interviewer_age](https://user-images.githubusercontent.com/42337253/194739982-0a929762-38f7-4701-8700-e2e54924d501.png)

![FU Month](https://user-images.githubusercontent.com/42337253/194738794-ef4593e5-fa2a-4c7e-9ff7-82ff1a7ef66a.png)


From this step observtion it can be concluded the features can be classified into two main groups, numerical features (such as  'Interviewer_WorkExperience', 'Interviewer_age','FU_Month' ) and categorical features (such as 'Eligible', 'Participant_gender', 'Participant_ethnicity', 'Intervention_group', 'City_code', 'Village_Cluster', 'Village_StateCode','Interviewer_Gender','Interviewer_Education', 'Interviewer_Ethnicity'). So, it is much better to investigate each group seprately.

### Categorical features
The obtained results from correlation calculation illustrate that, the relationship (based on Pearson and Spearman) between each categorical feature and our target is too weak. The investigation of last step figures more precisely show that, this is because the variation of classes in each feature is almost the same. In fact, each classes' mean in each feature are really close to each other. So, a good strategy to improve the classes' variation of each categorical feature is combining them with each other. Indeed, the idea is combining small differences to make more sensable variations. As an example, combination of three features, which belong to interviewer ('Interviewer_Gender','Interviewer_Education', 'Interviewer_Ethnicity') is proposed in the below picture. Comparison between the combined features' figure and each feature's figure separately can show the created variaton perfectlty. 



At the first, I made my real effort to creat all the possible combination of these features. For example, all the possible way to opt two features from ten and combining them, all the possible way to opt three features from ten and combining them, all the possible way to opt four features from ten and combining them and etc. I did this strategy to combine two, three, four and five features and I found it is not an efficient way because not only investigating all the combinations' figures takes a huge amount of time, but also it is almost impposible beacuse the variation of many combinations are really close to each other and chossing between them is not possible. More important, combining features with this manner will exponentialy increase numbmers of classes sepecifically from four features on. This section code is uploaded as 'Combining features and visualization'.   

Because of these issuses, we have to find a way to achieve maximum variation via combining the least numbers of features. Hence, 'the best variation creation' method and 'wisely combining feature' method were proposed. With regards to the former one, the features which have bigger differnce between thier classes' mean , are eligible to be opted for combination. The eligibility can be listed as follow:

1- City_code: it has three classes and difference among clasess are 0.08, 2.16 and 2.25.

2- Village_state_code: it has two classes and the difference between classes is 1.144.

3- Interviewer_education: it has three classes and difference among clasess are 0.669, 0.911 and 0.212.

4- Participant_ ethnicity: it has two classes and the difference between classes is 0.682.

5- Participant_ gender: it has two classes and the difference between classes is 0.645.

6- Interviention_ group: it has two classes and the difference between classes is 0.590.

7- Eligible: it has two classes and the difference between classes is 0.459.

8- Interviewer_gender: it has two classes and the difference between classes is 0.453.

9- Interviewer_ethnicity: it has two classes and the difference between classes is 0.433.

The combination's figure of respectively first three, four, five and six features of above list are presented below:

![Best two](https://user-images.githubusercontent.com/42337253/194742970-4aa5dd92-7c24-4ed2-8b1d-f3933ea730ff.png)

![Best three](https://user-images.githubusercontent.com/42337253/194742981-facd7c53-e9df-488d-b55e-763a4379107e.png)

![Best four](https://user-images.githubusercontent.com/42337253/194742989-efbadfee-5412-40a1-9dd6-01e8a9ced5b9.png)

![Best five](https://user-images.githubusercontent.com/42337253/194742995-a16da1ab-4bcb-4df3-929b-3022b788bd7b.png)

![Best six](https://user-images.githubusercontent.com/42337253/194743006-1e7f9e99-bb2c-4d60-b922-492580143541.png)

In terms of latter one, classifing categorical features into two groups of 'participant' and 'interviewer' and then removing features, which only increase numbers of classes and do not improve variation from each class, seems to be more rational. In terms of interviewer group, number of features which can be cinsidered as interviwer information is three ('Interviewer_Gender','Interviewer_Education', 'Interviewer_Ethnicity') and accordingly, the number of classes, which are created with this number of features is eleven. The combination's figure is demontrated in the following:



In terms of participnt class, number of features which can be cinsidered as participant information is six ('Eligible', 'Participant_gender', 'Participant_ethnicity', 'Intervention_group', 'City_code', 'Village_StateCode'). Because combination of these number of features can inrease number of classes exponantialy, we removed some of them which accordig the proposed list in 'the best variation creation' method cannot imporove variation too much.

Combintion of all features:

Combintion of five features (one of them were removed):

Combintion of four features (two of them were removed):



It is noteworthy mentioning that, having closer look at our data set indicates 'Village_Cluster' is not an independent feature.

## Numerical features


