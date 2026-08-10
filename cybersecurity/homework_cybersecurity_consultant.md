# Cybersecurity Consultant #

## Overview ##

Eagles Outdoor Gear is a small company with several employees who need access to different files and folders.

Your job is to act as the cybersecurity consultant who is helping the IT staff audit the system. You will examine users, groups, and permissions; identify mistakes; and then design a simple authorization system of your own.

Keep in mind that modern computer systems have many complex permissions, more than you need to know for this course. Most of the permissions can be categorized into three generic terms: *Read*, *Write*, and *Execute*. This assignment ignores any permission that fits under *Execute* and instead focuses on *Read* and *Write*. Also, keep in mind that having write permission means that you can create new files and modify existing ones.

Eagles Outdoor Gear has the following employees:

- Maya: Owner
- Luis: Accountant
- Priscilla: Sales Manager
- Evan: Sales Associate
- Jordan: Sales Associate
- Nora: Accounting Assistant
- Sofia: Summer Intern

The employees belong to these groups:

| Employee  | Groups                                |
| --------- | ------------------------------------- |
| Maya      | `Everyone`, `Managers`                |
| Luis      | `Everyone`, `Accounting Staff`        |
| Priscilla | `Everyone`, `Sales Staff`, `Managers` |
| Evan      | `Everyone`, `Sales Staff`             |
| Jordan    | `Everyone`, `Sales Staff`             |
| Nora      | `Everyone`                            |
| Sofia     | `Everyone`                            |

The company currently uses the following folders and permissions:

| Group            | `Sales` Folder | `Accounting` Folder | `Payroll` Folder |
| ---------------- | -------------- | ------------------- | ---------------- |
| Sales Staff      | Read/Write     | None                | None             |
| Accounting Staff | Read           | Read/Write          | None             |
| Managers         | Read/Write     | Read/Write          | Read/Write       |
| Everyone         | Read           | Read                | Read             |

In this authorization system, access rights are cumulative. So a user who has `Read` access from one group and `Write` access from another, will be granted both `Read` and `Write`. `None` means that the group grants neither `Read` nor `Write` permission, but it does not mean accesses from other groups are taken away.

## Diagnostic Questions ##

Answer the following:

1. Which employees can read the `Payroll` folder?

2. Which employees can modify files in the `Payroll` folder?

3. Which authorization plan best follows the principle of least privilege?
 - Put everyone in the Managers group so nobody has trouble accessing files.
 - Give every employee individual permissions to each folder based on their needs.
 - Give managers and department employees administrator access so they can fix permission problems themselves.
 - Place employees into groups based on their jobs and give each group the permissions needed for that job.

4. Nora has recently started working as the Accounting Assistant. She needs to update a spreadsheet in the `Accounting` folder, but the computer tells her that she does not have permission. What is the simplest appropriate change that would allow Nora to do her job?

5. Sofia, the summer intern, accidentally discovers that she can open the Payroll folder and see employee salary information. Why can Sofia see the Payroll folder and what permission should be changed to prevent this?

6. Although Luis is not a manager, as the head accountant he needs to change Nora's data in the `Payroll` folder. The owner, Maya, suggests solving the problem by adding him to the Managers group or granting him individual user account Read/Write permission directly to Nora's file. What is wrong with each solution? Can you suggest a better solution?

## Design Question ##

Eagles Outdoor Gear anticipates growth and has hired you as a full time IT-administrator to update its network with a cleaner authorization system.

The company has these folders:

- `Company Shared`
- `Sales`
- `Accounting`
- `Payroll`
- `Management`
- `IT Admin`

The following rules must be satisfied:

- Everyone may read the `Company Shared` folder.
- Sales employees may read and modify `Sales`.
- Priscilla needs the same Read/Write access to `Sales` as the sales associates. She also needs Read/Write access to `Payroll`.
- Only Maya needs access to `Management`.
- Luis and Nora may read and modify `Accounting`.
- Luis may read and modify the `Payroll` folder.
- Nora does not need access to `Payroll`.
- Maya needs access to all business folders.
- Sofia needs read-only access to Sales.
- You need access to `IT Admin` and whatever additional access is reasonably necessary for your job.
- Employees should not receive more access than they need.

Design a simple authorization system. Your design does not have to match one exact answer, but it should satisfy the requirements and follow the principle of least privilege.

### Part A: Groups ###

Create the groups you think Eagles should use and place employees into the appropriate groups. Don't forget to add yourself as the company's new IT-Administrator.

| Group          | Members        |
| -------------- | -------------- |
| `____________` | `____________` |
| `____________` | `____________` |
| `____________` | `____________` |

You may add rows as needed.

### Part B: Folder Permissions ###

Assign group permissions to each folder.

| Group          | `Company Shared` | `Sales`        | `Accounting`   | `Payroll`      | `Management`   | `IT Admin`     |
| -------------- | ---------------- | -------------- | -------------- | -------------- | -------------- | -------------- |
| `____________` | `____________`   | `____________` | `____________` | `____________` | `____________` | `____________` |
| `____________` | `____________`   | `____________` | `____________` | `____________` | `____________` | `____________` |
| `____________` | `____________`   | `____________` | `____________` | `____________` | `____________` | `____________` |

You may add rows as needed.
