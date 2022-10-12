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

![Eligible](https://user-images.githubusercontent.com/42337253/194745309-099e72bc-776e-4b38-a736-ed3bf48c3322.png)

![Intervention group](https://user-images.githubusercontent.com/42337253/194746407-9e5db350-4543-44bb-94dc-fd701ff548a3.png)

![Interviewer Ethnicity](https://user-images.githubusercontent.com/42337253/194746485-ee6b80c8-d800-4d70-947e-e9c3348e821c.png)

![Interviewer Gender](https://user-images.githubusercontent.com/42337253/194748210-61fccc57-7397-4a77-b726-da2c837a4e5a.png)

![Participant ethnicity](https://user-images.githubusercontent.com/42337253/194748224-6a5d20a9-e3ee-4af6-b0a3-2ebe3aa6fc0f.png)

![Participant gender](https://user-images.githubusercontent.com/42337253/194748404-906a43b6-b70f-4a98-ac22-78e382a06e00.png)

![Village StateCode](https://user-images.githubusercontent.com/42337253/194746736-b56fc43a-cad1-48b2-a4df-4d9836549d15.png)

![Interviewer Education](https://user-images.githubusercontent.com/42337253/194747938-bc0bad7f-b846-47fa-bc0e-92b74855cff7.png)

![City code](https://user-images.githubusercontent.com/42337253/194748009-4e82529b-3012-4241-92cc-95beff193a70.png)

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

Because of these issuses, we have to find a way to achieve maximum variation via combining the least numbers of features. Hence, 'the best variation creation' method and 'wisely combining feature' method were proposed. With regards to the former one, the features which have bigger differnce between thier classes' mean , are eligible to be opted for combination. The eligibility list is:

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

![Best two](https://user-images.githubusercontent.com/42337253/194744108-b3ef823e-1802-45bd-8809-651696081864.png)
![Best three](https://user-images.githubusercontent.com/42337253/194742981-facd7c53-e9df-488d-b55e-763a4379107e.png)
![Best four](https://user-images.githubusercontent.com/42337253/194742989-efbadfee-5412-40a1-9dd6-01e8a9ced5b9.png)
![Best five](https://user-images.githubusercontent.com/42337253/194742995-a16da1ab-4bcb-4df3-929b-3022b788bd7b.png)
![Best six](https://user-images.githubusercontent.com/42337253/194743006-1e7f9e99-bb2c-4d60-b922-492580143541.png)

In terms of latter one, classifing categorical features into two groups of 'participant' and 'interviewer' and then removing features, which only increase numbers of classes and do not improve variation from each class, seems to be more rational. In terms of interviewer group, number of features which can be cinsidered as interviwer information is three ('Interviewer_Gender','Interviewer_Education', 'Interviewer_Ethnicity') and accordingly, the number of classes, which are created with this number of features is eleven. The combination's figure is demontrated in the following:

![Three interviewer](https://user-images.githubusercontent.com/42337253/194744563-09d2937a-293e-42fe-a47f-478867e0affe.png)

In terms of participnt class, number of features which can be cinsidered as participant information is six ('Eligible', 'Participant_gender', 'Participant_ethnicity', 'Intervention_group', 'City_code', 'Village_StateCode'). Because combination of these number of features can inrease number of classes exponantialy, we removed some of them which accordig the proposed list in 'the best variation creation' method cannot imporove variation too much.

Combintion of all features:

![Six participant](https://user-images.githubusercontent.com/42337253/194744569-adab9904-1e7f-4f75-b5b6-4c8d7fbeacec.png)

Combintion of five features (one of them were removed):

![Five participant](https://user-images.githubusercontent.com/42337253/194744582-919df2e5-3187-4fee-a05d-322846962f2e.png)

Combintion of four features (two of them were removed):

![Four participant](https://user-images.githubusercontent.com/42337253/194744588-275da392-017b-49bb-b6a0-41e9332d2a4c.png)

It is noteworthy mentioning that, having closer look at our data set indicates 'Village_Cluster' is not an independent feature. This kind of feature combination is uploaded as 'Combining features and visualization- wisely'.

In order to find the best created features (ones which have stronger relation with target), some supervised algorithms were implemented. This is because these algorithms can consider even non linear relations. Finding relation between a categorical feature and a numerical target can be done through two manners. Firstly, considering this problem as a regression problem and using regression algorithm. Secondly, reversing the problem (considering our target as a feature and our feature as a target) and solving it as a classification problem. 

#### Two rgression solutions
In terms of using regression algortithms, two different approaches were considered: Applying linear regression and an Artificial Neural Network (ANN) based regression. In both methods, algorithms try to predict target using features (one by one). A featre will be selected, which its prediction (result of implementing regression algorithms on it) has a lower Mean Absolute Errore or Mean Squre Error. This part's code was uploaded as 'Regression categorical feature using linear regression.


Results of applying linear regression on features in 'best variation creation' group were proposed below. In additon, to make comparison improvement of regression algortithm's predication (when a new feature was combined), first the result of applying linear regression on 'City_ code', which was a feature with the maximum differences among clsasses' mean was perposed. Then, according eligibility list (presented earlier) features were combined (at the first, two first ones, then three first ones and etc), inear regression were applied and result was demonstrated.

MAE of City_code: 11.863

![21b](https://user-images.githubusercontent.com/42337253/195253595-d7840642-ccdf-4b4b-85a2-ce2665de1886.png)


MAE of Best_two: 11.862

![22b](https://user-images.githubusercontent.com/42337253/195253980-e7b6becd-0e8c-4de4-aa6f-95ad202c92a4.png)


MAE of Best_three: 11.863

![23b](https://user-images.githubusercontent.com/42337253/195254216-3f88fe64-5a12-4406-9f18-6613232c62a2.png)


MAE of Best_four: 11.870

![24b](https://user-images.githubusercontent.com/42337253/195254763-f632a217-4572-4997-b850-8cd47d9010aa.png)


MAE of Best_five: 11.870

![25b](https://user-images.githubusercontent.com/42337253/195255104-8beb4268-7201-494d-8321-6e5be34d67b7.png)


MAE of Best_six: 11.870

![62b](https://user-images.githubusercontent.com/42337253/195255402-7a62dabb-1132-42e7-b639-70e6ed06193c.png)


Also, results of applying ANN based regression on features in 'best variation creation' group were proposed here. The procedure is completely same as the last step but before proposing results, the applied archetecture were presented. This part's code was uploaded as 'Regression categorical feature using an ANN.

Validation MAE and Mse of City_code respectively: 11.8168 and  256.1124 

![11b](https://user-images.githubusercontent.com/42337253/195260054-3d03066c-99d2-4dc0-9d4a-a0c9d31b9145.png)

![loss](https://user-images.githubusercontent.com/42337253/195260060-c0b7c694-9991-410c-b297-aef85e983248.png)


Validation MAE and MSE of Best_two respectively: 11.7958 and 256.8635

![12b](https://user-images.githubusercontent.com/42337253/195259558-18720e2f-5118-42ed-91d0-3159b8957376.png)

![loss](https://user-images.githubusercontent.com/42337253/195259566-f5e3ae2a-3940-4ac5-88de-94461201b115.png)


Validation MAE and MSE of Best_three respectively: 11.7924 and 256.8034

![13b](https://user-images.githubusercontent.com/42337253/195261427-1005d6cb-a55c-4af4-80e3-2b3691682378.png)

![loss](https://user-images.githubusercontent.com/42337253/195261435-398ccb96-72a6-4091-aed1-b409d8481ef2.png)


Validation MAE and MSE of Best_four respectively: 11.7817 and 257.2674

![14b](https://user-images.githubusercontent.com/42337253/195268813-9ff37757-62d6-4023-a8b3-f0bb611892fb.png)

![loss](https://user-images.githubusercontent.com/42337253/195268816-b36c584b-48d2-45f4-b57d-570c5514e7f9.png)


Validation MAE and MSE of Best_five respectively: 11.7376 and 262.0800

![15b](https://user-images.githubusercontent.com/42337253/195271538-2009130d-db29-468c-9476-fe3f60e2df0b.png)

![loss](https://user-images.githubusercontent.com/42337253/195271549-8e3ae99f-85b9-4aac-9e41-7b590129189a.png)


Validation MAE and MSE of Best_six respectively: 11.7412 and 261.9711

![16b](https://user-images.githubusercontent.com/42337253/195272812-0b421fab-0954-4360-afd6-a4c695f12eac.png)

![loss](https://user-images.githubusercontent.com/42337253/195272829-70d28ebf-a472-427e-a423-6de131995527.png)




To sum up, all in all the result of applying ANN for regression porpuse was better than linear regression. This issue is obviouse from making comparison between their prediction visualization, MAE and MSE. This phenomenon shows the relation among our ctegorical features and target can be estimated better using non linear functions in comparison linear noes. To be more specific, both regression algorithms had better performance when it comes to combination of first three features of eligibility list and combining more features reduced the network performance. This is because average of classes (mean) is the key difference but it is not strong enough to make distiction among huge numbers of created classes.  


In the following a same procedure was used for 'wisely combining feature' group. The thing about this group was that algorithms show better performance on combining four features, which were about participants in comparison with combining three features, which were related to interviewers. Also, combining more than four features of participants decreased the network performcande and this is because the reason, discussed earlier. It is worth mentioning that as we expected the rsult of 'best variation creation' group was better than 'wisely combining feature' group, because its features were combined according eligibility list.


MAE of Four_participant (Linear regression): 11.869

![24p](https://user-images.githubusercontent.com/42337253/195283100-110c8572-c496-4cdd-8ed6-00da3e861092.png)


MAE of Five_participant (Linear regression): 11.866

![25p](https://user-images.githubusercontent.com/42337253/195283943-72c0aa30-a485-49d1-86a4-55da8b9eeb6f.png)


MAE of Six_participant (Linear regression): 11.867

![26p](https://user-images.githubusercontent.com/42337253/195284296-00df0dd1-c0a2-45a7-99a2-ff07ebb8f851.png)


MAE of Three_interviewer (Linear regression): 11.886
![23i](https://user-images.githubusercontent.com/42337253/195284902-b151bf61-a370-49e1-b21e-b876c474ed24.png)



Validation MAE and MSE of Four_participant (ANN based regression) respectively: 11.7897 and 256.5807  

![14p](https://user-images.githubusercontent.com/42337253/195276146-7433ae39-061b-4aa1-9f4a-e6f4cc9b0c23.png)

![loss](https://user-images.githubusercontent.com/42337253/195276145-b1afbb75-b315-41ad-a2c0-ba7989bf1642.png)


Validation MAE and MSE of Five_participant (ANN based regression) respectively: 11.7837 and 256.8120

![15p](https://user-images.githubusercontent.com/42337253/195277924-98207b2a-2846-4c5d-a613-b8939c934dde.png)

![loss](https://user-images.githubusercontent.com/42337253/195277954-b89973a3-bfa6-437f-8beb-e5355e4da3f1.png)


Validation MAE and MSE of Six_participant (ANN based regression) respectively: 11.7764 and 257.4860 

![16p](https://user-images.githubusercontent.com/42337253/195279494-7a16f1bc-db6e-4574-befc-a7a5efe4c67d.png)

![loss](https://user-images.githubusercontent.com/42337253/195279495-0d0bdf4e-8584-4364-bfe8-2711f6315617.png)


Validation MAE and MSE of Three_interviewer (ANN based regression) respectively: 11.8562 and 257.0421 

![13i](https://user-images.githubusercontent.com/42337253/195281776-1b913941-74f7-4be4-842d-5c771c07bc2b.png)

![loss](https://user-images.githubusercontent.com/42337253/195281790-bfbf9185-431f-4ad2-8749-0f7057363fd2.png)



#### Two classification solutions
We decided to solve this problem reverse to detect if there were any stronger relation. For this purpose two different approaches were employed, K-Neigherest Nighbour and an ANN. The first one is a simple but high speed classifier whereas second one is an accurate but slow. The results of applying KNN on 'best creation variation' group's fearures is prersented below. This section's script was uploaded as 'KNN classifier'.


Our ANN architecture was totaly same as the achitecture, used for regression pupose but there was a bit change in their hyperparameters. Indeed, we used accuracy as a metric instead of MSE and MAE. Also, we added a sigmoid activation function in its outputlayer. The results of applying ANN on 'best creation variation' group's fearures is displayed below. This part script was uploaded as 'ANN classifier'.


The results was not realy good and this issue cause us to do not continue to apply on other group and even other combinations in the 'best creation variation' group. In fact, combining features not only did not improve classification, but also make it worse. This is because the classifiers shoulod indicate each vlaue in our target belongs to which class. The thing is, the target's values were literally close to each other and they did not have a specific signature for exact classification pupose and cause our classifiers poor performance. Therefore, reversing problem to find relation was not a good strategy for this problem. Another interesting result, which was out of our expectation was better performance of KNN in comparison with ANN. This isuue shows that, eventhough ANN is a powerfull algorithm, whenever the data was not rich enough, this algorithm can not be trained properly and as a result its performance decreased. 


                                                       
 
### Numerical features

Based on correlation calculation, proposed earlier (Pearson and Spearman) the relation between numerical features such as 'Participant_age', 'Interviewer_WorkExperience', 'Interviewer_age' and our target is too weak, however 'FU_Month' shows strong relation with our target. In this part we decided to investigate this relation more precisely. In fact, the asssumption of existing a linear and non linear relation among our features and target were being investigated respectively via employing linear regression and an ANN based regression. It is worth mentioning that because both features and target are numerical, regression appraoch were opted and also because there was not any specific signature to make our numerical feature, categorical classification approaches to detec relation were not implemented.

In the following results of applying respectively, linear regression and ANN based regression were proposed. This section codes was uploaded as 'Regression numerical features using linear regression' and 'Regression numerical features using ANN'. 

MAE: 7.909
![ML-MAE 7 909](https://user-images.githubusercontent.com/42337253/194875334-ad306eab-b240-44c7-b9fd-6a23ef6c0899.png)


MAE: 11.964
![IL-MAE 11 964](https://user-images.githubusercontent.com/42337253/194875364-e2cba5fe-6f00-4b60-995a-af35385ecd5a.png)


MAE: 11.962
![IL-MAE 11 962](https://user-images.githubusercontent.com/42337253/194875403-10e0d228-22e6-4a63-b704-f5f59a361e8e.png)


MAE: 11.958
![PL- MAE 11 958](https://user-images.githubusercontent.com/42337253/194875440-e11f357a-1d62-43eb-88a7-43326eeb7a88.png)


MAE: 9.1214 and MSE: 211.0773
![MA-MAE 9 1214](https://user-images.githubusercontent.com/42337253/194884917-5bb88eb0-8ae0-4334-a0fe-541e716aeb58.png)

![MA-loss](https://user-images.githubusercontent.com/42337253/194885084-24b55266-fc8e-4974-952b-88967460ba80.png)


MAE: 12.3395 and MSE: 283.1067
![IA-MAE 12 3395](https://user-images.githubusercontent.com/42337253/194896763-d3aef625-350d-4490-a1ce-738c63f762fc.png)

![IL-loss](https://user-images.githubusercontent.com/42337253/194887485-2219e56f-ab4c-4dd8-8baa-a72ed16411bd.png)

MAE: 12.3941 and MSE: 284.2482
![IA-MAE 12 3941](https://user-images.githubusercontent.com/42337253/194896910-960af78d-642d-4d02-8978-3159f8770e52.png)

![IL-loss](https://user-images.githubusercontent.com/42337253/194890210-346ea06f-97d1-4e0f-a5ba-70fa670192c3.png)


MAE: 12.4319 and MSE: 288.4689
![PA- MAE 12 4319](https://user-images.githubusercontent.com/42337253/194897002-0f96b956-38ba-4b3e-a237-94aa8544474c.png)


![PA- loss](https://user-images.githubusercontent.com/42337253/194894449-14d80096-4953-49ca-9e78-3d0e58ba4aa2.png)


Interesting issue is better performance of linear regression in comparison with ANN. This is because, the relation between our numerical features and target is linear and almost there is not any non linear relation. 

                                                             
