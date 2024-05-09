import { createQueue } from 'kue';
import { expect } from 'chai';
import sinon from 'sinon';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', function() {
  const queue = createQueue({ name: 'push_notification_code_test' });

  beforeEach(function () {
    queue.testMode.enter(true);
  });
  afterEach(function () {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', function () {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('Jobs is not an array');
  });

  it('should create two new jobs to the queue', function () {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);

    const [job1, job2] = queue.testMode.jobs;

    expect(job1.type).to.equal('push_notification_code_3');
    expect(job1.data).to.eql(jobs[0]);
    expect(job2.type).to.equal('push_notification_code_3');
    expect(job2.data).to.eql(jobs[1]);
  });

  it('should log appropriate messages for each job event', function () {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      }
    ];

    const consoleSpy = sinon.spy(console, 'log');
    createPushNotificationsJobs(jobs, queue);

    const job = queue.testMode.jobs[0];
    job.id = 1;

    job.emit('enqueue');
    job.emit('complete');
    job.emit('failed', new Error('Some error'));
    job.emit('progress', 50);

    expect(consoleSpy.calledWith('Notification job created:', job.id)).to.be.true;
    expect(consoleSpy.calledWith('Notification job', job.id, 'completed')).to.be.true;
    expect(consoleSpy.calledWith('Notification job', job.id, 'failed:', 'Some error')).to.be.true;
    expect(consoleSpy.calledWith('Notification job', job.id, '50% complete')).to.be.true;

    consoleSpy.restore();
  });
});
