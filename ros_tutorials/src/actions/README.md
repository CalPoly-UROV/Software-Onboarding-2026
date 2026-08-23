# ROS Action Example

This package contains a simple action example for an assignment where the server sleeps for a requested amount of time.

## Action definition structure

A ROS action file has three sections:

1. Goal
2. Result
3. Feedback

The sections are separated by `---` lines.

```action
# Goal
duration seconds
---
# Result
bool success
---
# Feedback
duration remaining
```

### Meaning
- The client sends a goal with a sleep duration.
- The server sleeps for that amount of time.
- The server reports whether the action completed successfully.
- The server can also send feedback while it is sleeping, such as the remaining time.

This is the basic pattern used in ROS action communication:

- goal: request sent from client to server
- feedback: periodic status updates while the action runs
- result: final outcome returned when the action finishes

For this assignment, the action can be named `SleepFor` and the file can be saved as `sleep_for.action` inside the actions package.
