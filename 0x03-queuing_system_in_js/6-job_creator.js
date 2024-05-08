import { createQueue } from 'kue';

const queue = createQueue({name: 'push_notification_code'});

const jobData = {
  phoneNumber: '0643526182',
  message: 'This is the code to verify your account',
};

const job = queue.create('push_notification_code', jobData);

job.on('enqueue', () => {
  console.log('Notification job created:', job.id);
}).on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed');
});

job.save();
