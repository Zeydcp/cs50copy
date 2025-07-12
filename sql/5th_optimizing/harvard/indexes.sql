CREATE INDEX "enrollment_student_index" ON "enrollments" ("student_id");

CREATE INDEX "enrollment_course_index" ON "enrollments" ("course_id");

CREATE INDEX "number_index" ON "courses" ("number");

CREATE INDEX "semester_index" ON "courses" ("semester");

CREATE INDEX "satisfy_course_index" ON "satisfies" ("course_id");
