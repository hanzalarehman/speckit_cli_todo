# Tasks: Phase I - CLI Todo

**Input**: Design documents from `/specs/001-phase-i-cli-todo/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), data-model.md

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project directory structure per plan.md
- [X] T002 [P] Create src/__init__.py and tests/__init__.py
- [X] T003 [P] Create src/models/__init__.py and src/cli/__init__.py
- [X] T004 [P] Create tests/unit/__init__.py

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**CRITICAL**: No user story work can begin until this phase is complete

- [X] T005 Create TaskStatus enum in src/models/task.py (data-model.md: TaskStatus Enum)
- [X] T006 Create Task dataclass in src/models/task.py (data-model.md: Task Entity)
- [X] T007 [P] Create unit tests for Task dataclass in tests/unit/test_task.py
- [X] T008 Create in-memory storage module in src/cli/storage.py (plan.md: Storage)
- [X] T009 [P] Create unit tests for storage in tests/unit/test_storage.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Task (Priority: P1)

**Goal**: Users can add new tasks with non-empty text

**Independent Test**: Add a task and verify it appears in list

### Tests for User Story 1

> Write these tests FIRST, ensure they FAIL before implementation

- [X] T010 [P] [US1] Test add_task creates task with pending status in tests/unit/test_operations.py
- [X] T011 [P] [US1] Test add_task rejects empty text in tests/unit/test_operations.py
- [X] T012 [P] [US1] Test add_task assigns unique ID in tests/unit/test_operations.py

### Implementation for User Story 1

- [X] T013 [US1] Implement add_task function in src/cli/operations.py (plan.md: Task CRUD operations)
- [X] T014 [US1] Implement get_task_text helper in src/cli/menu.py (plan.md: Task Text Input Pattern)
- [X] T015 [US1] Implement add task menu option in src/cli/menu.py (spec.md: User Story 1)
- [X] T016 [US1] Add integration test for complete add task flow in tests/unit/test_menu.py

**Checkpoint**: User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Task List (Priority: P1)

**Goal**: Users can view all tasks with their ID, text, and status

**Independent Test**: View tasks after adding them

### Tests for User Story 2

> Write these tests FIRST, ensure they FAIL before implementation

- [X] T017 [P] [US2] Test view_tasks returns all tasks in tests/unit/test_operations.py
- [X] T018 [P] [US2] Test view_tasks shows empty message when no tasks in tests/unit/test_operations.py

### Implementation for User Story 2

- [X] T019 [US2] Implement list_tasks function in src/cli/operations.py (plan.md: Task CRUD operations)
- [X] T020 [US2] Implement display_tasks function in src/cli/menu.py (spec.md: User Story 2)
- [X] T021 [US2] Implement view tasks menu option in src/cli/menu.py (spec.md: User Story 2)
- [X] T022 [US2] Add integration test for view tasks flow in tests/unit/test_menu.py

**Checkpoint**: User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Update Task (Priority: P1)

**Goal**: Users can modify task text for existing tasks

**Independent Test**: Change task text and verify the change

### Tests for User Story 3

> Write these tests FIRST, ensure they FAIL before implementation

- [X] T023 [P] [US3] Test update_task changes text in tests/unit/test_operations.py
- [X] T024 [P] [US3] Test update_task rejects empty text in tests/unit/test_operations.py
- [X] T025 [P] [US3] Test update_task raises error for non-existent ID in tests/unit/test_operations.py

### Implementation for User Story 3

- [X] T026 [US3] Implement update_task function in src/cli/operations.py (plan.md: Task CRUD operations)
- [X] T027 [US3] Implement get_task_id helper in src/cli/menu.py (plan.md: Task ID Input Pattern)
- [X] T028 [US3] Implement update task menu option in src/cli/menu.py (spec.md: User Story 3)
- [X] T029 [US3] Add integration test for update task flow in tests/unit/test_menu.py

**Checkpoint**: User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Delete Task (Priority: P2)

**Goal**: Users can remove tasks by ID

**Independent Test**: Remove a task and verify it no longer appears

### Tests for User Story 4

> Write these tests FIRST, ensure they FAIL before implementation

- [X] T030 [P] [US4] Test delete_task removes task in tests/unit/test_operations.py
- [X] T031 [P] [US4] Test delete_task raises error for non-existent ID in tests/unit/test_operations.py

### Implementation for User Story 4

- [X] T032 [US4] Implement delete_task function in src/cli/operations.py (plan.md: Task CRUD operations)
- [X] T033 [US4] Implement delete task menu option in src/cli/menu.py (spec.md: User Story 4)
- [X] T034 [US4] Add integration test for delete task flow in tests/unit/test_menu.py

**Checkpoint**: User Stories 1-4 should all work independently

---

## Phase 7: User Story 5 - Mark Task Complete (Priority: P1)

**Goal**: Users can mark pending tasks as complete

**Independent Test**: Mark a task complete and verify status change

### Tests for User Story 5

> Write these tests FIRST, ensure they FAIL before implementation

- [X] T035 [P] [US5] Test mark_complete changes status to completed in tests/unit/test_operations.py
- [X] T036 [P] [US5] Test mark_complete is idempotent in tests/unit/test_operations.py

### Implementation for User Story 5

- [X] T037 [US5] Implement mark_complete function in src/cli/operations.py (plan.md: Task CRUD operations)
- [X] T038 [US5] Implement mark complete menu option in src/cli/menu.py (spec.md: User Story 5)
- [X] T039 [US5] Add integration test for mark complete flow in tests/unit/test_menu.py

**Checkpoint**: User Stories 1-5 should all work independently

---

## Phase 8: User Story 6 - Mark Task Incomplete (Priority: P2)

**Goal**: Users can mark completed tasks as pending

**Independent Test**: Change a task from complete to pending

### Tests for User Story 6

> Write these tests FIRST, ensure they FAIL before implementation

- [X] T040 [P] [US6] Test mark_incomplete changes status to pending in tests/unit/test_operations.py
- [X] T041 [P] [US6] Test mark_incomplete is idempotent in tests/unit/test_operations.py

### Implementation for User Story 6

- [X] T042 [US6] Implement mark_incomplete function in src/cli/operations.py (plan.md: Task CRUD operations)
- [X] T043 [US6] Implement mark incomplete menu option in src/cli/menu.py (spec.md: User Story 6)
- [X] T044 [US6] Add integration test for mark incomplete flow in tests/unit/test_menu.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 9: Application Flow & Error Handling

**Purpose**: Integration of menu loop and error handling across all operations

### Tests for Application Flow

- [X] T045 [P] Test get_menu_choice validates input in tests/unit/test_menu.py
- [X] T046 [P] Test error messages for invalid operations in tests/unit/test_menu.py

### Implementation

- [X] T047 Create main menu display function in src/cli/menu.py (plan.md: Main Menu Loop)
- [X] T048 Create get_menu_choice function in src/cli/menu.py (plan.md: Input Handling Pattern)
- [X] T049 Create application entry point in src/cli/app.py (plan.md: CLI Control Flow)
- [X] T050 Integrate all menu options in main loop (plan.md: Main Menu Loop)
- [X] T051 Add error handling wrapper in app.py (plan.md: Error Handling Strategy)

---

## Phase 10: Polish & Cross-Cutting Concerns

**Purpose**: Final validation and documentation

- [X] T052 Run full test suite and verify all tests pass
- [X] T053 Verify quickstart.md instructions work correctly
- [X] T054 [P] Create requirements.txt (empty - no dependencies)
- [X] T055 [P] Add README.md to src/cli/ directory if needed

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phases 3-8)**: All depend on Foundational phase completion
  - User stories can proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Application Flow (Phase 9)**: Depends on all user stories complete
- **Polish (Phase 10)**: Depends on all previous phases complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational - No dependencies on other stories
- **User Story 3 (P1)**: Can start after Foundational - No dependencies on other stories
- **User Story 4 (P2)**: Can start after Foundational - No dependencies on other stories
- **User Story 5 (P1)**: Can start after Foundational - No dependencies on other stories
- **User Story 6 (P2)**: Can start after Foundational - No dependencies on other stories

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Operations functions before menu integration
- Menu integration before application flow
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel
- All tests for a user story marked [P] can run in parallel
- Different user stories can be worked on in parallel

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. STOP and VALIDATE: Test User Story 1 independently
5. Demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Demo (MVP!)
3. Add User Story 2 → Test independently → Demo
4. Continue with remaining stories
5. Each story adds value without breaking previous stories

---

## Artifact References

| Artifact | Path | Purpose |
|----------|------|---------|
| Specification | `specs/001-phase-i-cli-todo/spec.md` | User stories, requirements |
| Technical Plan | `specs/001-phase-i-cli-todo/plan.md` | Architecture, structure |
| Data Model | `specs/001-phase-i-cli-todo/data-model.md` | Entity definitions |
| Quickstart | `specs/001-phase-i-cli-todo/quickstart.md` | Usage guide |

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies
