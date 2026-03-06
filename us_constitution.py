"""
US Constitution - Structured and Chunked for Legal Chatbot
Source: National Archives (archives.gov) - Public Domain
"""

from legal_chatbot import LegalDocument

# Preamble
PREAMBLE = LegalDocument(
    id="const_preamble",
    title="US Constitution - Preamble",
    content="""We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America.""",
    source="US Constitution, Preamble",
    jurisdiction="Federal"
)

# Article I - Legislative Branch
ARTICLE_I_SEC_1 = LegalDocument(
    id="const_art1_sec1",
    title="Article I, Section 1 - Legislative Powers",
    content="""All legislative Powers herein granted shall be vested in a Congress of the United States, which shall consist of a Senate and House of Representatives.""",
    source="US Constitution, Article I, Section 1",
    jurisdiction="Federal"
)

ARTICLE_I_SEC_8 = LegalDocument(
    id="const_art1_sec8",
    title="Article I, Section 8 - Powers of Congress",
    content="""The Congress shall have Power To lay and collect Taxes, Duties, Imposts and Excises, to pay the Debts and provide for the common Defence and general Welfare of the United States; but all Duties, Imposts and Excises shall be uniform throughout the United States;

To borrow Money on the credit of the United States;

To regulate Commerce with foreign Nations, and among the several States, and with the Indian Tribes;

To establish an uniform Rule of Naturalization, and uniform Laws on the subject of Bankruptcies throughout the United States;

To coin Money, regulate the Value thereof, and of foreign Coin, and fix the Standard of Weights and Measures;

To provide for the Punishment of counterfeiting the Securities and current Coin of the United States;

To establish Post Offices and post Roads;

To promote the Progress of Science and useful Arts, by securing for limited Times to Authors and Inventors the exclusive Right to their respective Writings and Discoveries;

To constitute Tribunals inferior to the supreme Court;

To define and punish Piracies and Felonies committed on the high Seas, and Offences against the Law of Nations;

To declare War, grant Letters of Marque and Reprisal, and make Rules concerning Captures on Land and Water;

To raise and support Armies, but no Appropriation of Money to that Use shall be for a longer Term than two Years;

To provide and maintain a Navy;

To make Rules for the Government and Regulation of the land and naval Forces;

To provide for calling forth the Militia to execute the Laws of the Union, suppress Insurrections and repel Invasions;

To provide for organizing, arming, and disciplining, the Militia, and for governing such Part of them as may be employed in the Service of the United States, reserving to the States respectively, the Appointment of the Officers, and the Authority of training the Militia according to the discipline prescribed by Congress;

To exercise exclusive Legislation in all Cases whatsoever, over such District (not exceeding ten Miles square) as may, by Cession of particular States, and the Acceptance of Congress, become the Seat of the Government of the United States, and to exercise like Authority over all Places purchased by the Consent of the Legislature of the State in which the Same shall be, for the Erection of Forts, Magazines, Arsenals, dock-Yards, and other needful Buildings;—And

To make all Laws which shall be necessary and proper for carrying into Execution the foregoing Powers, and all other Powers vested by this Constitution in the Government of the United States, or in any Department or Officer thereof.""",
    source="US Constitution, Article I, Section 8",
    jurisdiction="Federal"
)

# Article II - Executive Branch
ARTICLE_II_SEC_1 = LegalDocument(
    id="const_art2_sec1",
    title="Article II, Section 1 - Executive Power and Presidential Qualifications",
    content="""The executive Power shall be vested in a President of the United States of America. He shall hold his Office during the Term of four Years, and, together with the Vice President, chosen for the same Term, be elected, as follows:

Each State shall appoint, in such Manner as the Legislature thereof may direct, a Number of Electors, equal to the whole Number of Senators and Representatives to which the State may be entitled in the Congress: but no Senator or Representative, or Person holding an Office of Trust or Profit under the United States, shall be appointed an Elector.

No Person except a natural born Citizen, or a Citizen of the United States, at the time of the Adoption of this Constitution, shall be eligible to the Office of President; neither shall any Person be eligible to that Office who shall not have attained to the Age of thirty five Years, and been fourteen Years a Resident within the United States.""",
    source="US Constitution, Article II, Section 1",
    jurisdiction="Federal"
)

ARTICLE_II_SEC_2 = LegalDocument(
    id="const_art2_sec2",
    title="Article II, Section 2 - Presidential Powers",
    content="""The President shall be Commander in Chief of the Army and Navy of the United States, and of the Militia of the several States, when called into the actual Service of the United States; he may require the Opinion, in writing, of the principal Officer in each of the executive Departments, upon any Subject relating to the Duties of their respective Offices, and he shall have Power to grant Reprieves and Pardons for Offences against the United States, except in Cases of Impeachment.

He shall have Power, by and with the Advice and Consent of the Senate, to make Treaties, provided two thirds of the Senators present concur; and he shall nominate, and by and with the Advice and Consent of the Senate, shall appoint Ambassadors, other public Ministers and Consuls, Judges of the supreme Court, and all other Officers of the United States, whose Appointments are not herein otherwise provided for, and which shall be established by Law: but the Congress may by Law vest the Appointment of such inferior Officers, as they think proper, in the President alone, in the Courts of Law, or in the Heads of Departments.""",
    source="US Constitution, Article II, Section 2",
    jurisdiction="Federal"
)

# Article III - Judicial Branch
ARTICLE_III_SEC_1 = LegalDocument(
    id="const_art3_sec1",
    title="Article III, Section 1 - Judicial Power",
    content="""The judicial Power of the United States, shall be vested in one supreme Court, and in such inferior Courts as the Congress may from time to time ordain and establish. The Judges, both of the supreme and inferior Courts, shall hold their Offices during good Behaviour, and shall, at stated Times, receive for their Services, a Compensation, which shall not be diminished during their Continuance in Office.""",
    source="US Constitution, Article III, Section 1",
    jurisdiction="Federal"
)

ARTICLE_III_SEC_2 = LegalDocument(
    id="const_art3_sec2",
    title="Article III, Section 2 - Scope of Judicial Power",
    content="""The judicial Power shall extend to all Cases, in Law and Equity, arising under this Constitution, the Laws of the United States, and Treaties made, or which shall be made, under their Authority;—to all Cases affecting Ambassadors, other public Ministers and Consuls;—to all Cases of admiralty and maritime Jurisdiction;—to Controversies to which the United States shall be a Party;—to Controversies between two or more States;— between a State and Citizens of another State,—between Citizens of different States,—between Citizens of the same State claiming Lands under Grants of different States, and between a State, or the Citizens thereof, and foreign States, Citizens or Subjects.

The Trial of all Crimes, except in Cases of Impeachment, shall be by Jury; and such Trial shall be held in the State where the said Crimes shall have been committed; but when not committed within any State, the Trial shall be at such Place or Places as the Congress may by Law have directed.""",
    source="US Constitution, Article III, Section 2",
    jurisdiction="Federal"
)

# Bill of Rights
AMENDMENT_1 = LegalDocument(
    id="const_amend1",
    title="First Amendment - Freedom of Religion, Speech, Press, Assembly, Petition",
    content="""Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the Government for a redress of grievances.""",
    source="US Constitution, Amendment I",
    jurisdiction="Federal"
)

AMENDMENT_2 = LegalDocument(
    id="const_amend2",
    title="Second Amendment - Right to Bear Arms",
    content="""A well regulated Militia, being necessary to the security of a free State, the right of the people to keep and bear Arms, shall not be infringed.""",
    source="US Constitution, Amendment II",
    jurisdiction="Federal"
)

AMENDMENT_3 = LegalDocument(
    id="const_amend3",
    title="Third Amendment - Quartering of Soldiers",
    content="""No Soldier shall, in time of peace be quartered in any house, without the consent of the Owner, nor in time of war, but in a manner to be prescribed by law.""",
    source="US Constitution, Amendment III",
    jurisdiction="Federal"
)

AMENDMENT_4 = LegalDocument(
    id="const_amend4",
    title="Fourth Amendment - Search and Seizure",
    content="""The right of the people to be secure in their persons, houses, papers, and effects, against unreasonable searches and seizures, shall not be violated, and no Warrants shall issue, but upon probable cause, supported by Oath or affirmation, and particularly describing the place to be searched, and the persons or things to be seized.""",
    source="US Constitution, Amendment IV",
    jurisdiction="Federal"
)

AMENDMENT_5 = LegalDocument(
    id="const_amend5",
    title="Fifth Amendment - Due Process, Self-Incrimination, Double Jeopardy",
    content="""No person shall be held to answer for a capital, or otherwise infamous crime, unless on a presentment or indictment of a Grand Jury, except in cases arising in the land or naval forces, or in the Militia, when in actual service in time of War or public danger; nor shall any person be subject for the same offence to be twice put in jeopardy of life or limb; nor shall be compelled in any criminal case to be a witness against himself, nor be deprived of life, liberty, or property, without due process of law; nor shall private property be taken for public use, without just compensation.""",
    source="US Constitution, Amendment V",
    jurisdiction="Federal"
)

AMENDMENT_6 = LegalDocument(
    id="const_amend6",
    title="Sixth Amendment - Right to Fair Trial",
    content="""In all criminal prosecutions, the accused shall enjoy the right to a speedy and public trial, by an impartial jury of the State and district wherein the crime shall have been committed, which district shall have been previously ascertained by law, and to be informed of the nature and cause of the accusation; to be confronted with the witnesses against him; to have compulsory process for obtaining witnesses in his favor, and to have the Assistance of Counsel for his defence.""",
    source="US Constitution, Amendment VI",
    jurisdiction="Federal"
)

AMENDMENT_7 = LegalDocument(
    id="const_amend7",
    title="Seventh Amendment - Civil Trial by Jury",
    content="""In Suits at common law, where the value in controversy shall exceed twenty dollars, the right of trial by jury shall be preserved, and no fact tried by a jury, shall be otherwise re-examined in any Court of the United States, than according to the rules of the common law.""",
    source="US Constitution, Amendment VII",
    jurisdiction="Federal"
)

AMENDMENT_8 = LegalDocument(
    id="const_amend8",
    title="Eighth Amendment - Cruel and Unusual Punishment",
    content="""Excessive bail shall not be required, nor excessive fines imposed, nor cruel and unusual punishments inflicted.""",
    source="US Constitution, Amendment VIII",
    jurisdiction="Federal"
)

AMENDMENT_9 = LegalDocument(
    id="const_amend9",
    title="Ninth Amendment - Rights Retained by the People",
    content="""The enumeration in the Constitution, of certain rights, shall not be construed to deny or disparage others retained by the people.""",
    source="US Constitution, Amendment IX",
    jurisdiction="Federal"
)

AMENDMENT_10 = LegalDocument(
    id="const_amend10",
    title="Tenth Amendment - Powers Reserved to States",
    content="""The powers not delegated to the United States by the Constitution, nor prohibited by it to the States, are reserved to the States respectively, or to the people.""",
    source="US Constitution, Amendment X",
    jurisdiction="Federal"
)

AMENDMENT_11 = LegalDocument(
    id="const_amend11",
    title="Eleventh Amendment - Suits Against States",
    content="""The Judicial power of the United States shall not be construed to extend to any suit in law or equity, commenced or prosecuted against one of the United States by Citizens of another State, or by Citizens or Subjects of any Foreign State.""",
    source="US Constitution, Amendment XI (1795)",
    jurisdiction="Federal"
)

AMENDMENT_12 = LegalDocument(
    id="const_amend12",
    title="Twelfth Amendment - Electoral College Procedures",
    content="""The Electors shall meet in their respective states and vote by ballot for President and Vice-President, one of whom, at least, shall not be an inhabitant of the same state with themselves; they shall name in their ballots the person voted for as President, and in distinct ballots the person voted for as Vice-President, and they shall make distinct lists of all persons voted for as President, and of all persons voted for as Vice-President, and of the number of votes for each, which lists they shall sign and certify, and transmit sealed to the seat of the government of the United States, directed to the President of the Senate.""",
    source="US Constitution, Amendment XII (1804)",
    jurisdiction="Federal"
)

AMENDMENT_13 = LegalDocument(
    id="const_amend13",
    title="Thirteenth Amendment - Abolition of Slavery",
    content="""Section 1. Neither slavery nor involuntary servitude, except as a punishment for crime whereof the party shall have been duly convicted, shall exist within the United States, or any place subject to their jurisdiction. This amendment abolished slavery and freed enslaved people.

Section 2. Congress shall have power to enforce this article by appropriate legislation.

Historical context: Ratified in 1865 after the Civil War, this was the first of the Reconstruction Amendments that ended slavery in America.""",
    source="US Constitution, Amendment XIII (1865)",
    jurisdiction="Federal"
)

AMENDMENT_14 = LegalDocument(
    id="const_amend14",
    title="Fourteenth Amendment - Equal Protection and Due Process",
    content="""All persons born or naturalized in the United States, and subject to the jurisdiction thereof, are citizens of the United States and of the State wherein they reside. No State shall make or enforce any law which shall abridge the privileges or immunities of citizens of the United States; nor shall any State deprive any person of life, liberty, or property, without due process of law; nor deny to any person within its jurisdiction the equal protection of the laws.""",
    source="US Constitution, Amendment XIV, Section 1 (1868)",
    jurisdiction="Federal"
)

AMENDMENT_15 = LegalDocument(
    id="const_amend15",
    title="Fifteenth Amendment - Voting Rights Regardless of Race",
    content="""Section 1. The right of citizens of the United States to vote shall not be denied or abridged by the United States or by any State on account of race, color, or previous condition of servitude. This amendment extended voting rights to African American men and all citizens regardless of race.

Section 2. The Congress shall have power to enforce this article by appropriate legislation.

Historical context: Ratified in 1870 after the Civil War, this was one of the Reconstruction Amendments.""",
    source="US Constitution, Amendment XV (1870)",
    jurisdiction="Federal"
)

AMENDMENT_16 = LegalDocument(
    id="const_amend16",
    title="Sixteenth Amendment - Income Tax",
    content="""The Congress shall have power to lay and collect taxes on incomes, from whatever source derived, without apportionment among the several States, and without regard to any census or enumeration.""",
    source="US Constitution, Amendment XVI (1913)",
    jurisdiction="Federal"
)

AMENDMENT_17 = LegalDocument(
    id="const_amend17",
    title="Seventeenth Amendment - Direct Election of Senators",
    content="""The Senate of the United States shall be composed of two Senators from each State, elected by the people thereof, for six years; and each Senator shall have one vote. The electors in each State shall have the qualifications requisite for electors of the most numerous branch of the State legislatures.""",
    source="US Constitution, Amendment XVII (1913)",
    jurisdiction="Federal"
)

AMENDMENT_18 = LegalDocument(
    id="const_amend18",
    title="Eighteenth Amendment - Prohibition (Repealed)",
    content="""Section 1. After one year from the ratification of this article the manufacture, sale, or transportation of intoxicating liquors within, the importation thereof into, or the exportation thereof from the United States and all territory subject to the jurisdiction thereof for beverage purposes is hereby prohibited.

Section 2. The Congress and the several States shall have concurrent power to enforce this article by appropriate legislation.

Note: This amendment was repealed by the Twenty-first Amendment.""",
    source="US Constitution, Amendment XVIII (1919, repealed 1933)",
    jurisdiction="Federal"
)

AMENDMENT_19 = LegalDocument(
    id="const_amend19",
    title="Nineteenth Amendment - Women's Suffrage and Voting Rights",
    content="""The right of citizens of the United States to vote shall not be denied or abridged by the United States or by any State on account of sex. This amendment guarantees women the right to vote.

Congress shall have power to enforce this article by appropriate legislation.

Historical context: Ratified in 1920, this amendment extended voting rights to women, prohibiting any denial of suffrage based on sex or gender.""",
    source="US Constitution, Amendment XIX (1920)",
    jurisdiction="Federal"
)

AMENDMENT_20 = LegalDocument(
    id="const_amend20",
    title="Twentieth Amendment - Presidential Term and Succession",
    content="""Section 1. The terms of the President and Vice President shall end at noon on the 20th day of January, and the terms of Senators and Representatives at noon on the 3d day of January, of the years in which such terms would have ended if this article had not been ratified; and the terms of their successors shall then begin.

Section 3. If, at the time fixed for the beginning of the term of the President, the President elect shall have died, the Vice President elect shall become President.""",
    source="US Constitution, Amendment XX (1933)",
    jurisdiction="Federal"
)

AMENDMENT_21 = LegalDocument(
    id="const_amend21",
    title="Twenty-first Amendment - Repeal of Prohibition",
    content="""Section 1. The eighteenth article of amendment to the Constitution of the United States is hereby repealed.

Section 2. The transportation or importation into any State, Territory, or possession of the United States for delivery or use therein of intoxicating liquors, in violation of the laws thereof, is hereby prohibited.""",
    source="US Constitution, Amendment XXI (1933)",
    jurisdiction="Federal"
)

AMENDMENT_22 = LegalDocument(
    id="const_amend22",
    title="Twenty-second Amendment - Presidential Term Limits",
    content="""Section 1. No person shall be elected to the office of the President more than twice, and no person who has held the office of President, or acted as President, for more than two years of a term to which some other person was elected President shall be elected to the office of the President more than once.""",
    source="US Constitution, Amendment XXII (1951)",
    jurisdiction="Federal"
)

AMENDMENT_23 = LegalDocument(
    id="const_amend23",
    title="Twenty-third Amendment - DC Electoral Votes",
    content="""Section 1. The District constituting the seat of Government of the United States shall appoint in such manner as the Congress may direct: A number of electors of President and Vice President equal to the whole number of Senators and Representatives in Congress to which the District would be entitled if it were a State, but in no event more than the least populous State.""",
    source="US Constitution, Amendment XXIII (1961)",
    jurisdiction="Federal"
)

AMENDMENT_24 = LegalDocument(
    id="const_amend24",
    title="Twenty-fourth Amendment - Poll Tax Prohibition",
    content="""Section 1. The right of citizens of the United States to vote in any primary or other election for President or Vice President, for electors for President or Vice President, or for Senator or Representative in Congress, shall not be denied or abridged by the United States or any State by reason of failure to pay any poll tax or other tax.

Section 2. The Congress shall have power to enforce this article by appropriate legislation.""",
    source="US Constitution, Amendment XXIV (1964)",
    jurisdiction="Federal"
)

AMENDMENT_25 = LegalDocument(
    id="const_amend25",
    title="Twenty-fifth Amendment - Presidential Succession and Disability",
    content="""Section 1. In case of the removal of the President from office or of his death or resignation, the Vice President shall become President.

Section 2. Whenever there is a vacancy in the office of the Vice President, the President shall nominate a Vice President who shall take office upon confirmation by a majority vote of both Houses of Congress.

Section 3. Whenever the President transmits to the President pro tempore of the Senate and the Speaker of the House of Representatives his written declaration that he is unable to discharge the powers and duties of his office, and until he transmits to them a written declaration to the contrary, such powers and duties shall be discharged by the Vice President as Acting President.

Section 4. Whenever the Vice President and a majority of either the principal officers of the executive departments or of such other body as Congress may by law provide, transmit to the President pro tempore of the Senate and the Speaker of the House of Representatives their written declaration that the President is unable to discharge the powers and duties of his office, the Vice President shall immediately assume the powers and duties of the office as Acting President.""",
    source="US Constitution, Amendment XXV (1967)",
    jurisdiction="Federal"
)

AMENDMENT_26 = LegalDocument(
    id="const_amend26",
    title="Twenty-sixth Amendment - Voting Age Lowered to 18",
    content="""Section 1. The right of citizens of the United States, who are eighteen years of age or older, to vote shall not be denied or abridged by the United States or by any State on account of age. This amendment lowered the voting age from 21 to 18 years old.

Section 2. The Congress shall have power to enforce this article by appropriate legislation.

Historical context: Ratified in 1971 during the Vietnam War era, based on the principle that those old enough to be drafted should be able to vote.""",
    source="US Constitution, Amendment XXVI (1971)",
    jurisdiction="Federal"
)

AMENDMENT_27 = LegalDocument(
    id="const_amend27",
    title="Twenty-seventh Amendment - Congressional Compensation",
    content="""No law, varying the compensation for the services of the Senators and Representatives, shall take effect, until an election of Representatives shall have intervened.""",
    source="US Constitution, Amendment XXVII (1992)",
    jurisdiction="Federal"
)

# Collection of all documents
ALL_CONSTITUTION_DOCS = [
    PREAMBLE,
    ARTICLE_I_SEC_1,
    ARTICLE_I_SEC_8,
    ARTICLE_II_SEC_1,
    ARTICLE_II_SEC_2,
    ARTICLE_III_SEC_1,
    ARTICLE_III_SEC_2,
    AMENDMENT_1,
    AMENDMENT_2,
    AMENDMENT_3,
    AMENDMENT_4,
    AMENDMENT_5,
    AMENDMENT_6,
    AMENDMENT_7,
    AMENDMENT_8,
    AMENDMENT_9,
    AMENDMENT_10,
    AMENDMENT_11,
    AMENDMENT_12,
    AMENDMENT_13,
    AMENDMENT_14,
    AMENDMENT_15,
    AMENDMENT_16,
    AMENDMENT_17,
    AMENDMENT_18,
    AMENDMENT_19,
    AMENDMENT_20,
    AMENDMENT_21,
    AMENDMENT_22,
    AMENDMENT_23,
    AMENDMENT_24,
    AMENDMENT_25,
    AMENDMENT_26,
    AMENDMENT_27,
]


def load_constitution(knowledge_base):
    """Load all Constitution documents into the knowledge base"""
    for doc in ALL_CONSTITUTION_DOCS:
        knowledge_base.add_document(doc)
    return len(ALL_CONSTITUTION_DOCS)
