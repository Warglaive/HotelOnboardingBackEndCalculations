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
| Description | 1. Actor  |
| Precondition | None |
| Scenario | 1. The system requests an email address from the actor <br> 2. The actor submits their email address <br> 3. The system notifies the actor that the email address is now saved |
| Result | Save actor's email address |
| Exceptions |TBD  |
| Extensions | N/A  |

| 3. Hotel name | Hotel manager fills in hotel name |
| --- | --- |
| Actor | Hotel manager |
| Description | 1. Actor  |
| Precondition | 1. Email address <br> |
| Scenario | 1. Actor fills in the hotel name <br> 2. The system checks if the hotel exists in the database and pre-fills all the fields <br> 3. The actor sees all the pre-filled fields <br> 4. The system requests approval if each of the fields is up-to-date <br> 5. The actor approves/denies or edits the data |
| Result | Hotel data filled in successfully |
| Exceptions | 1. Hotel does not exist<br> 2.  |
| Extensions | If the hotel does not exist -> actor fills in data manually  |

| 4. Optional(Exclusive) details | Hotel manager fills in optional(Exclusive) hotel details |
| --- | --- |
| Actor | Hotel manager |
| Description | 1. Actor  |
| Precondition | 1. Email address <br> 2. Hotel name |
| Scenario | 1. System asks the actor for any hotel exclusive and/or optional details <br> 2. Actor fills in any hotel exclusive and/or optional details |
| Result | Exclusive/optional hotel data filled in successfully |
| Exceptions | 1. Hotel does not exist<br> 2. No exclusive features <br> 3. No optional features |
| Extensions | TBD |

| 5. Onboard(Submit) Hotel | Hotel manager onboards hotel |
| --- | --- |
| Actor | Hotel manager |
| Description | 1. Actor  |
| Precondition | 1. Email address <br> 2. Hotel name <br> |
| Scenario | 1. System presents the actor with an overview of all the filled in hotel details and email address <br> 2. Actor decides to edit any of the data or to submit the data <br> 3. If edit -> actor is allowed to modify details <br> 4. If submit -> System registers the hotel in the database <br> 5. System displays the onboarded hotel page |
| Result | Hotel onboarded successfully|
| Exceptions | TBD |
| Extensions | TBD |
#
| 6. Upload photos | Hotel manager uploads hotel photos |
| --- | --- |
| Actor | Hotel manager |
| Description | 1. Actor  |
| Precondition | 1. Email address <br> 2. Hotel name |
| Scenario | 1. System asks the actor for any hotel exclusive and/or optional details <br> 2. Actor fills in any hotel exclusive and/or optional details |
| Result | Exclusive/optional hotel data filled in successfully |
| Exceptions | 1. Hotel does not exist<br> 2. No exclusive features <br> 3. No optional features |
| Extensions | TBD |
##