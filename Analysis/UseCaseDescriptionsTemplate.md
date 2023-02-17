## Hotel Manger
| 1. Calculator | Hotel manager uses revenue calculator |
| --- | --- |
| Actor | Hotel manager |
| Description | Hotel manager uses revenue calculator |
| Precondition |  None |
| Scenario | 1. Actor access the webpage. <br> 2. Actor fills in each detail of the calculator <br> 3. Actor select "Calculate" option <br> 4. System returns estimated revenue |
| Result | Estimated revenue increase is presented to the actor |
| Exceptions |TBD  |
| Extensions | 1. Actor is adviced to fill in email address |

| 2. Email address | Hotel manager fills in email address |
| --- | --- |
| Actor | Hotel manager |
| Description | Hotel manager fills in email address  |
| Precondition | None |
| Scenario | 1. The system requests an email address from the actor <br> 2. The actor submits their email address <br> 3. The system notifies the actor that the email address is now saved |
| Result | Save actor's email address |
| Exceptions |TBD  |
| Extensions | N/A  |

| 3. Hotel name | Hotel manager fills in hotel name |
| --- | --- |
| Actor | Hotel manager |
| Description | Hotel manager fills in hotel name  |
| Precondition | 1. Email address <br> |
| Scenario | 1. Actor fills in the hotel name <br> 2. The system checks if the hotel exists in the database and pre-fills all the fields <br> 3. The actor sees all the pre-filled fields <br> 4. The system requests approval if each of the fields is up-to-date <br> 5. The actor approves/denies or edits the data |
| Result | Hotel data filled in successfully |
| Exceptions | 1. Hotel does not exist|
| Extensions | If the hotel does not exist -> actor fills in data manually  |

| 4. Optional(Exclusive) details | Hotel manager fills in optional(Exclusive) hotel details |
| --- | --- |
| Actor | Hotel manager |
| Description | Hotel manager fills in optional(Exclusive) hotel details  |
| Precondition | 1. Email address <br> 2. Hotel name |
| Scenario | 1. System asks the actor for any hotel exclusive and/or optional details <br> 2. Actor fills in any hotel exclusive and/or optional details |
| Result | Exclusive/optional hotel data filled in successfully |
| Exceptions | 1. Hotel does not exist<br> 2. No exclusive features <br> 3. No optional features |
| Extensions | TBD |

| 5. Onboard(Submit) Hotel | Hotel manager onboards hotel |
| --- | --- |
| Actor | Hotel manager |
| Description | Hotel manager onboards hotel  |
| Precondition | 1. Email address <br> 2. Hotel name <br> |
| Scenario | 1. System presents the actor with an overview of all the filled in hotel details and email address <br> 2. Actor decides to edit any of the data or to submit the data <br> 3a. If edit -> actor is allowed to modify details <br> 3b. If submit -> System registers the hotel in the database <br> 4. System displays the onboarded hotel page |
| Result | Hotel onboarded successfully|
| Exceptions | TBD |
| Extensions | TBD |

| 6. Upload photos | Hotel manager uploads hotel photos |
| --- | --- |
| Actor | Hotel manager |
| Description | Hotel manager uploads hotel photos  |
| Precondition | 1. Onboard(Submit) Hotel |
| Scenario | 1. System urges the actor to upload photos <br> 2. Actor selects photos to be uploaded from multiple sources <br> 3. System stores the photos <br> 4. System prompts ViaLuxury for approval of the photos 5. ViaLuxury approves the photos 6. System visualizes the photos on the onboarded hotel page  |
| Result | Photos are successfully uploaded and visualized |
| Exceptions | 1. Invalid photo format exception <br> 2. Photo size exception <br> |
| Extensions | TBD |

| 7. Contact ViaLuxury | Hotel manager contacts ViaLuxury representative |
| --- | --- |
| Actor | Hotel manager |
| Description | Hotel manager contacts ViaLuxury representative |
| Precondition | 1. Onboard(Submit) Hotel |
| Scenario | 1. Actor access contact page <br> 2. System displays multiple contact options <br> 3. Actor selects an option <br> 4. System connects the actor to the ViaLuxury representative |
| Result | Actor successfully contacts ViaLuxury representative |
| Exceptions | 1. Contact option not available at the moment <br> |
| Extensions | TBD |

| 8. Update facilities | Hotel manager updates available hotel facilities |
| --- | --- |
| Actor | Hotel manager |
| Description | Hotel manager updates available hotel facilities |
| Precondition | 1. Onboard(Submit) Hotel |
| Scenario | 1. Actor navigates to facilities overview <br> 2. System displays all facilities <br> 3. Actor selects a single facility 4. System displays multiple options (edit, delete, disable, other) <br> 5. Actor selects to edit selected facility <br> 5. System prompts the actor to add new data <br> 6. Actor updates the selected facility with new data <br> 6. System applies and visualizes the changes |
| Result | Facility updated successfully |
| Exceptions | TBD |
| Extensions | TBD |

| 9. Approve/deny changes proposed by ViaLuxury | Hotel manager approves/denies changes |
| --- | --- |
| Actor | Hotel manager |
| Description | Hotel manager approves/denies changes proposed by ViaLuxury |
| Precondition | 1. Onboard(Submit) Hotel |
| Scenario |  |
| Result | Facility updated successfully |
| Exceptions | TBD |
| Extensions | TBD |
##

| 10. Create employee account | Hotel manager creates account |
| --- | --- |
| Actor | Hotel manager |
| Description | Hotel manager creates Front-Desk or other employee account |
| Precondition | 1. Onboard(Submit) Hotel |
| Scenario | 1.  |
| Result | Facility updated successfully |
| Exceptions | TBD |
| Extensions | TBD |


##
| 11. Grant priviliges | Hotel manager grants priviliges |
| --- | --- |
| Actor | Hotel manager |
| Description | Hotel manager grants priviliges to Hotel Employee |
| Precondition | 1. Onboard(Submit) Hotel |
| Scenario |  |
| Result | Facility updated successfully |
| Exceptions | TBD |
| Extensions | TBD |