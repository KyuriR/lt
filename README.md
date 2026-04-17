Kyuri Reddy

TESTS DONE
1. BASIC CASE: Checked that the program works correctly when the columns are in the expected order.  
2. REORDERED COLUMNS: Made sure the program can still find the "Student Number" and "Mark" columns even if they appear in a different order.  
3. EDGE CASE - LAST ROW HIGHEST: Verified that the program correctly identifies the top student when the highest mark is in the last row of the file.  

These tests were chosen to make sure that the program correctly detects column positions instead of assuming a fixed order and that it can find the highest mark and that edge don’t break the program.  

ERRORS FOUND
- The column index was not being incremented properly, so the wrong columns were being used.  
- The program was not updating the student number (`best_idx`) when a higher mark was found.  
- An undefined variable (`student_num`) was being used in the code.  
- The script was running automatically when imported, which caused errors during testing.  

CHANGES TO CODE
- Fixed the column indexing by correctly incrementing the index in the loop.  
- Updated the logic so that both the highest mark and the corresponding student number are stored correctly.  
- Defined and used the correct variable student_num
- Wrapped the main execution code in:
if __name__ == "__main__":