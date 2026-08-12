Keane Benedict Z. Urbano
9-Platinum
Annex A

Scenario

The PSHS school canteen is small and often gets crowded during lunch break. Students line up to buy food, but the process is slow because:

Some students take too long to decide what to order.
The cashier has to manually calculate totals and give change.
There is no system to track which food items are running out.
Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.

Step 1: Identify the Big Problem

Main Problem: The canteen system is inefficient and leads to longer waiting time for all.

Step 2: Identify three to four Sub-Problems
Please list possible sub-problems:

1. Ordering Bottleneck:
      Students spend too much time looking at the menu and deciding what to order at the front of the line.

2. Manual Payment Handling
      The cashier manually inputs cost calculate totals and handles physical money(coins and bills) which slows down and takes time per transaction.
   
3. No Dedicated Stock System
      The canteen lacks a dedicated stock system that monitor stock levels in real time leading to unexpected delays or cancellation of orders while waiting for delivery.

4. No Proper Line
      There is no physical or organized way to line up leading to chaotic operation that includes cutting in line and 'pasabay'.

Step 3: Define Computational Thinking Approaches
For each sub-problem, apply CT skills:

1. CT Skill: Pattern Recognition
     Canteen staff can use pattern recognition to see what processes during lining up leads to students taking more time to order. They can use these data to fix the bottleneck with numerous solutions ex: Placing boards with available items in the line area so before ordering students know what is available to order.

2. CT Skill: Abstraction
     Cashiers can speed things up by having a computerized payment system and hides complex backround details and only displays two essential numbers to the cashier: Total Due and Change Required.

3. CT Skills: Algorithm Design

Canteen staff can create a dedicated system that has a database and whenever an item is bought, subtract 1 from the inventory; if the total stock goes below 10, automatically send an alert to the kitchen to prepare more food or order more food.

4. CT Skills: Algorithm Design

Staff can create a strict rule set for queuing, setting up physical markings for a single line, sending out numbered order tickets, and have a display/person showing call out numbers so students only move forward when it is their number.

Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem

Problem 1-4
START
```
   // Step 1: Address Ordering Bottleneck & Menu
    DISPLAY Menu_Board with Available_Items
    PROMPT Student to select food items

    // Step 2: Address Stock Management System
    FOR EACH Selected_Item IN Student_Order:
        IF Stock[Selected_Item] > 0 THEN
            ADD Selected_Item TO Cart
            UPDATE Total_Due = Total_Due + Item_Price
            DECREASE Stock[Selected_Item] BY 1
            
            // Check for low stock alert
            IF Stock[Selected_Item] < 5 THEN
                SEND Low_Stock_Alert TO Kitchen
            ENDIF
        ELSE
            DISPLAY "Item Out of Stock. Please select another item."
        ENDIF
    ENDFOR

    // Step 3: Address Payment Handling (Abstraction)
    DISPLAY Total_Due ON POS_Screen
    PROMPT Student for Payment (Cash or Card)
    
    IF Payment_Received >= Total_Due THEN
        CALCULATE Change_Required = Payment_Received - Total_Due
        DISPLAY Change_Required ON Screen
        
        // Step 4: Address Line Chaos & Queue System
        GENERATE Queue_Ticket_Number
        DISPLAY "Order Confirmed. Your Ticket Number is: " + Queue_Ticket_Number
        SEND Order_Details TO Kitchen_Pickup_Screen
    ELSE
        DISPLAY "Insufficient Payment. Transaction Cancelled."
    ENDIF
END
```

Step 5: Reflection/Explanation:
Solving this scenario helped me improve my skills in both github and CT skills. It also taught me how to make a folder in github. Now decomposing canteen overcrowding into smaller sub-problems made a massive issue manageable. Because of CT skills we didn't do random guesses but we applied specific CT skills to each sub-problem Pattern Recognition to spot ordering delays, Abstraction to simplify the cashier's display, Decomposition to automate stock alerts, and Algorithm Design to control queue flow. Breaking down the system allowed us to create a fast, organized canteen experience with minimal wait times.
     

