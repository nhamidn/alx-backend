import { createQueue, Job } from 'kue';

const BlacklistedPhoneNumbers = ['4153518780', '4153518781'];
const queue = createQueue();

const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100);
  if (BlacklistedPhoneNumbers.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  }
  console.log(
    `Sending notification to ${phoneNumber},`,
    `with message: ${message}`,
  );
  job.progress(50, 100);
  done();
};

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
