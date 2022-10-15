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


Validation MAE of City_code: 0.7421693643199738 

![11b(0 7421693643199738)](https://user-images.githubusercontent.com/42337253/195918579-d38ba56f-e3e3-4456-a3ce-2b9bcb984f35.png)

![loss(0 7421693643199738)](https://user-images.githubusercontent.com/42337253/195918633-cfb40873-2fb4-4eaf-9096-46c0d6f81c8b.png)


Validation MAE of Best_two: 0.7415406365835382

![12b(0 7415406365835382)](https://user-images.githubusercontent.com/42337253/195918828-62b136aa-bfd5-4501-888f-fffc0727920e.png)

![loss(0 7415406365835382)](https://user-images.githubusercontent.com/42337253/195918852-54b8d7dc-7c46-4663-8ed4-e997c153492c.png)


Validation MAE of Best_three: 0.742745038042128

![13b(0 742745038042128)](https://user-images.githubusercontent.com/42337253/195919190-b038a870-e297-4d4f-ad93-23c5ba846f13.png)

![loss(0 742745038042128)](https://user-images.githubusercontent.com/42337253/195919203-4053800b-a047-4504-afff-0180ce930115.png)



Validation MAE of Best_four: 0.7431747175569832

![14b(0 7431747175569832)](https://user-images.githubusercontent.com/42337253/195919330-b8a94d2e-1fd5-49b4-90e3-362abd390b2d.png)

![loss(0 7431747175569832)](https://user-images.githubusercontent.com/42337253/195919336-68fe1fad-d077-4bb9-be5e-8ab55e16b838.png)


Validation MAE of Best_five: 0.7433048499085942 

![15b(0 7433048499085942)](https://user-images.githubusercontent.com/42337253/195919577-89d02422-4e73-4514-b8b8-72362a6ea9d9.png)

![loss(0 7433048499085942)](https://user-images.githubusercontent.com/42337253/195919636-d36a55e6-56f5-4184-a4b1-d5f4d287c903.png)


Validation MAE of Best_six: 0.7441807791097875

![16b(0 7441807791097875)](https://user-images.githubusercontent.com/42337253/195920000-93310e07-cf88-4552-b8ba-1f12d1654288.png)

![loss(0 7441807791097875)](https://user-images.githubusercontent.com/42337253/195920007-389015cb-13b9-458c-9af8-3662852960d6.png)



To sum up, all in all the result of applying ANN for regression porpuse was better than linear regression (the figure below can prove this issue). This issue is obviouse from making comparison between their prediction visualization, MAE and MSE. This phenomenon shows the relation among our ctegorical features and target can be estimated better using non linear functions in comparison linear noes. To be more specific, both regression algorithms had better performance when it comes to combination of first three features of eligibility list and combining more features reduced the network performance. This is because average of classes (mean) is the key difference but it is not strong enough to make distiction among huge numbers of created classes.  

![Linear regression vs ANN- Best three](https://user-images.githubusercontent.com/42337253/195352417-046e64c7-99bb-42a5-927d-a6392ebcf6b0.png)

![City_code vs Best_two](https://user-images.githubusercontent.com/42337253/195921158-f3b099ac-19e8-43a5-b1de-2970e5e2bdef.png)


In the following a same procedure was used for 'wisely combining feature' group. The thing about this group was that algorithms show better performance on combining four features, which were about participants in comparison with combining three features, which were related to interviewers. Also, combining more than four features of participants decreased the network performcande and this is because the reason, discussed earlier. It is worth mentioning that as we expected the rsult of 'best variation creation' group was better than 'wisely combining feature' group, because its features were combined according eligibility list.


MAE of Four_participant (Linear regression): 11.869

![24p](https://user-images.githubusercontent.com/42337253/195283100-110c8572-c496-4cdd-8ed6-00da3e861092.png)


MAE of Five_participant (Linear regression): 11.866

![25p](https://user-images.githubusercontent.com/42337253/195283943-72c0aa30-a485-49d1-86a4-55da8b9eeb6f.png)


MAE of Six_participant (Linear regression): 11.867

![26p](https://user-images.githubusercontent.com/42337253/195284296-00df0dd1-c0a2-45a7-99a2-ff07ebb8f851.png)


MAE of Three_interviewer (Linear regression): 11.886
![23i](https://user-images.githubusercontent.com/42337253/195284902-b151bf61-a370-49e1-b21e-b876c474ed24.png)



Validation MAE of Four_participant (ANN based regression): 0.7436238367965747  

![14p(0 7436238367965747)](https://user-images.githubusercontent.com/42337253/195993429-41794cb5-9100-460e-b16a-0ecfdd5b7936.png)


![loss(0 7436238367965747)](https://user-images.githubusercontent.com/42337253/195993432-81266c81-cdc4-4383-b5d9-92dbdd328300.png)


Validation MAE of Five_participant (ANN based regression): 0.7436517098824937

![15p(0 7436517098824937)](https://user-images.githubusercontent.com/42337253/195993482-12e08c9a-4f81-4cb9-8b3f-d748c5f04f96.png)

![loss (0 7436517098824937)](https://user-images.githubusercontent.com/42337253/195993488-edd2847e-6897-4b83-b73f-897a69de3cf9.png)


Validation MAE of Six_participant (ANN based regression): 0.7440071549946741

![16p(0 7440071549946741)](https://user-images.githubusercontent.com/42337253/195993530-596b53e6-6f4c-471f-bbc5-0bfdd54aed1a.png)

![loss(0 7440071549946741)](https://user-images.githubusercontent.com/42337253/195993533-52d79b7b-8fcc-4147-8c3f-4e3316b11608.png)


Validation MAE of Three_interviewer: 0.7436813963040475

![13i(0 7436813963040475)](https://user-images.githubusercontent.com/42337253/195993566-d7936d6a-952d-45c0-a229-24ea8652b64f.png)

![loss (0 7436813963040475)](https://user-images.githubusercontent.com/42337253/195993572-69218554-7314-4a7f-84d4-d178218f4378.png)




#### Two classification solutions
We decided to solve this problem reverse to detect if there were any stronger relation. For this purpose two different approaches were employed, K-Neigherest Nighbour and an ANN. The first one is a simple but high speed classifier whereas second one is an accurate but slow. The results of applying KNN on 'best creation variation' group's fearures is prersented below. This section's script was uploaded as 'KNN classifier'.

City_code:

![acc](https://user-images.githubusercontent.com/42337253/195297918-e23df95b-fc04-4996-8c4d-dd5b2b0c1d01.PNG)

![City_code_1](https://user-images.githubusercontent.com/42337253/195298571-886af286-edf9-412a-b5e1-971c81a1a49b.png)

Best_two:

![acc](https://user-images.githubusercontent.com/42337253/195301267-c4fd41df-cee1-4154-87cc-5ae2c6c21704.PNG)

![Best_two](https://user-images.githubusercontent.com/42337253/195301278-59b5342b-6e0c-4678-943a-4d013d97704b.png)

Best_three:

![acc](https://user-images.githubusercontent.com/42337253/195301928-c30c5bd5-edec-432f-8253-1fe52c1cce50.PNG)

![Best_three](https://user-images.githubusercontent.com/42337253/195301940-de93e9ec-23bb-4460-9b15-e09a2e88676e.png)

Best_four:

![acc](https://user-images.githubusercontent.com/42337253/195304274-837c7111-1a6a-4a83-8d4a-740e2268963e.PNG)

![Best_four](https://user-images.githubusercontent.com/42337253/195304285-9640e4d1-e12d-4b5c-ba07-65b4178e3380.png)




Our ANN architecture was totaly same as the achitecture, used for regression pupose but there was a bit change in their hyperparameters. Indeed, we used accuracy as a metric instead of MSE and MAE. Also, we added a sigmoid activation function in its outputlayer. The results of applying ANN on 'best creation variation' group's fearures is displayed below. This part script was uploaded as 'ANN classifier'.

City_code:

![acc](https://user-images.githubusercontent.com/42337253/195314930-f0f8d07e-e658-40de-b28c-b5e1fa412ec3.PNG)
![City_code](https://user-images.githubusercontent.com/42337253/195314915-d3babc1f-f000-43e0-a0d4-82570a309d63.png)

Best_two:

![acc](https://user-images.githubusercontent.com/42337253/195336808-44b23074-cbfa-4cb9-b985-a64c19d43b76.PNG)
![Best_two](https://user-images.githubusercontent.com/42337253/195335566-b8c67bc1-6b0b-4ce3-9d86-84456644b4f3.png)


Best_three:

![acc](https://user-images.githubusercontent.com/42337253/195337291-98541e75-1968-4211-9467-2fa02c412d81.PNG)
![Best_two](https://user-images.githubusercontent.com/42337253/195337296-79ee33e2-1b98-4c9e-baa1-bb09a9d4d8dd.png)


Best_four:

![acc](https://user-images.githubusercontent.com/42337253/195341148-b44b5a58-d278-4b26-9edb-1186dbfee3bc.PNG)
![Best_four](https://user-images.githubusercontent.com/42337253/195341150-90ebc51f-a303-4c08-a7e4-c6e1f0651bff.png)




The results was not realy good and this issue cause us to do not continue to apply on another group and even other combinations in the 'best creation variation' group. In fact, combining features not only did not improve classification, but also make it worse. This is because the classifiers shoulod indicate each vlaue in our target belongs to which class. The thing is, the target's values were literally close to each other and they did not have a specific signature for exact classification pupose and cause our classifiers poor performance. Therefore, reversing problem to find relation was not a good strategy for this problem. Another interesting result, which was out of our expectation was better performance of KNN in comparison with ANN. This isuue shows that, eventhough ANN is a powerfull algorithm, whenever the data was not rich enough, this algorithm can not be trained properly and as a result its performance decreased. 


                                                       
 
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


                                                             
