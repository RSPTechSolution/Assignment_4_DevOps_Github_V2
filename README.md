# Git Branching, Merging, Reset, and Rebase Assignment
### Overview

This assignment demonstrates practical Git workflows used in real-world development.
It covers branch creation, feature development, backend integration, merging, resetting commits, and rebasing while preserving commit history.

The work is divided logically between frontend and backend branches and finally integrated into the main branch.

### Branch Structure

main – Stable branch where final, tested changes are merged.

master_1 – Frontend development branch.

master_2 – Backend API development branch.

Both master_1 and master_2 were created from the main branch.

## Part 1: Feature Development
Frontend Development (master_1)

In the master_1 branch, a To-Do Page was created in the frontend.

The page contains a form with the following fields:

Item Name

Item Description

This branch focuses only on UI and frontend logic.

Backend Development (master_2)

In the master_2 branch, a backend API route was implemented.

Route Name: 
POST /submittodoitem

Merging to main

After completing development:

Changes from master_1 were merged into main.

Changes from master_2 were merged into main.

At this point, the main branch contained both frontend and backend functionality.

## Part 2: Enhancing the To-Do Form (master_1)

Further enhancements were made only in the master_1 branch.

New Fields Added

* Item ID

* Item UUID

* Item Hash

Commit Strategy

Each field was added and committed individually to maintain a clean and traceable history:

* First commit – Added Item ID field

* Second commit – Added Item UUID field

* Third commit – Added Item Hash field

## Git Reset and Commit Deletion
To demonstrate Git reset:
The main branch was reset back to the commit where only the Item ID field existed.
```git reset --soft``` was used so that file changes remained staged.
This state was then re-committed to the main branch.
This shows how to safely roll back commits without losing work.

### Rebasing Changes

To synchronize branches properly:

The updated main branch was rebased onto master_1.

Rebasing was done without squashing commits, preserving individual commit history.

This ensures that each logical change remains visible and traceable.
