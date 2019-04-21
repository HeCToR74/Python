/*
* constants for Analytics.js
*/
export const InitialDataBarChart = [{
                label: 'somethingC',
                values: [
                    {x: 'SomethingA', y: 0},
                    {x: 'SomethingB', y: 0},
                    {x: 'SomethingC', y: 0}
                ]
         }];
export const ConstDayMonthYear = ["7 Days", "Month", "Year"];
export const InitialCurrentType =  "7 Days";

/*
* constants for CreateInterview.js
*/
export const tempDate = new Date();
export const date =
                  tempDate.getFullYear() +
                  "-" +
                  (tempDate.getMonth() + 1) +
                  "-" +
                  tempDate.getDate() +
                  " " +
                  tempDate.getHours() +
                  ":" +
                  tempDate.getMinutes() +
                  ":" +
                  tempDate.getSeconds();
export const currDate = "Current Date= " + date;
/*
* constants for PasswordReset.js and PasswordResetConfirm.js
*/
export const expRegPass = /(?=.*[0-9])(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{6,}/g;
/*
* constants for PasswordChange.js
*/
export const expRegEmail =  /^([a-zA-Z0-9]+)@([a-zA-Z0-9]+)\.([a-zA-Z]{2,5})$/g;
/*
* constants for Profile.js
*/
export const config = {
  bucketName: process.env.bucketName,
  region: process.env.region,
  accessKeyId: process.env.accessKeyId,
  secretAccessKey: process.env.secretAccessKey,
};
/*
* constants for ExpertResult.js
*/
export const listLevel = [
  {
    id: 1,
    value: 'Trainee',
    label: 'Trainee',
  },
  {
    id: 2,
    value: 'Junior low',
    label: 'Junior low',
  },
  {
    id: 3,
    value: 'Junior',
    label: 'Junior',
  },
  {
    id: 4,
    value: 'Junior strong',
    label: 'Junior strong',
  },
  {
    id: 5,
    value: 'Intermediate low',
    label: 'Intermediate low',
  },
  {
    id: 6,
    value: 'Intermediate',
    label: 'Intermediate',
  },
  {
    id: 7,
    value: 'Intermediate strong',
    label: 'Intermediate strong',
  },
  {
    id: 8,
    value: 'Senior low',
    label: 'Senior low',
  },
  {
    id: 3,
    value: 'Senior',
    label: 'Senior',
  },
  {
    id: 9,
    value: 'Senior strong',
    label: 'Senior strong',
  },
  {
    id: 3,
    value: 'Leader low',
    label: 'Leader low',
  },
  {
    id: 10,
    value: 'Leader',
    label: 'Leader',
  },
];
export const englishLevel = [
  {
    id: 1,
    value: 'Elementary',
    label: 'Elementary',
  },
  {
    id: 2,
    value: 'Pre-intermediate',
    label: 'Pre-intermediate',
  },
  {
    id: 3,
    value: 'Intermediate',
    label: 'Intermediate',
  },
  {
    id: 4,
    value: 'Upper-intermediate',
    label: 'Upper-intermediate',
  },
  {
    id: 5,
    value: 'Advanced',
    label: 'Advanced',
  },
];
export const listHighPotential =[
  {
    id: 1,
    value: 'Low potential',
    label: 'Low potential',
  },
  {
    id: 2,
    value: 'Regular',
    label: 'Regular',
  },
  {
    id: 3,
    value: 'High potential',
    label: 'High potential',
  },
];
export const listPotential = [
  {
    id: 1,
    value: 'Hire',
    label: 'Hire',
  },
  {
    id: 2,
    value: 'Not hire',
    label: 'Not hire',
  },
];
/*
* constants for  MapModal.js
*/
export const API_KEY = process.env.geocode_api_key;
/*
* constants for  .js
*/






