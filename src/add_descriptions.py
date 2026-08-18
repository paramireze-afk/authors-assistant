import re, os

# Map of file path -> description to inject
DESCRIPTIONS = {
    "articles/synthesis/2026-08-09-bill-ackman.md": "The story of Bill Ackman's billion-dollar public short against Herbalife, the multi-level marketing giant he called a pyramid scheme, and the long, strange fight that followed.",
    "articles/synthesis/2026-08-09-follow-the-money.md": "How pro-Israel political money actually moves in American elections — PACs, bundlers, AIPAC's structure, and what the spending patterns show about institutional influence.",
    "articles/synthesis/2026-08-09-nikola-trucking.md": "The rise and fall of Nikola Corporation: Trevor Milton's fraud, the short-seller Hindenburg Research, and the financial and legal machinery that surrounded the prosecution.",
    "articles/synthesis/2026-08-09-prohibition.md": "The argument that Prohibition was as much a fight over industrial alcohol and fuel competition as a moral crusade — and what that reframe reveals about who backed it.",
    "articles/synthesis/2026-08-10-ai-bubble.md": "Why 2006, not 2008, was the year the housing bubble was already over — and what the AI investment cycle looks like when you apply the same framework.",
    "articles/synthesis/2026-08-10-rag-tagg.md": "How Rag Tagg built a devoted audience by turning Apex Legends gameplay into something closer to serialized storytelling, and what that says about parasocial media.",
    "articles/synthesis/2026-08-12-joe-rogan-and-ufc.md": "How the legalization of sports betting reshaped the UFC's relationship with its audience, its broadcast partners, and the way fights are framed and sold.",
    "articles/synthesis/opec-beginners-guild.md": "A beginner's guide to OPEC: what the cartel actually is, how it tries to manage global oil prices, why it often fails, and how geopolitics shapes every barrel.",
    "knowledge/books/fools-errand.md": "Notes on Scott Horton's case for ending the war in Afghanistan — the history of U.S. involvement, the warlord economy it created, and why the mission was unwinnable from the start.",
    "knowledge/books/funding-the-enemy.md": "Notes on Douglas Wissing's investigation into how U.S. reconstruction contracts and military spending inadvertently financed the Taliban insurgency in Afghanistan.",
    "knowledge/books/ghost-wars.md": "Notes on Steve Coll's definitive history of the CIA's involvement in Afghanistan from the Soviet invasion through September 10, 2001, and the covert networks it built and lost.",
    "knowledge/books/maos-great-famine.md": "Notes on Frank Dikötter's history of the famine caused by Mao's Great Leap Forward — the political decisions, the falsified grain statistics, and the death toll.",
    "knowledge/books/princes-of-yen.md": "Notes on Richard Werner's account of how the Bank of Japan's window guidance policy deliberately engineered Japan's bubble economy and the deflation that followed.",
    "knowledge/books/rape-of-the-mind.md": "Notes on Joost Meerloo's framework for menticide — the systematic destruction of independent thought through psychological manipulation, coercion, and conditioning.",
    "knowledge/books/salt.md": "Notes on Mark Kurlansky's history of salt as a driver of trade, warfare, preservation technology, and political economy across civilizations.",
    "knowledge/books/the-real-anthony-fauci.md": "Notes on Robert F. Kennedy Jr.'s critical account of Anthony Fauci's leadership of NIAID, his relationships with pharmaceutical industry partners, and his handling of COVID-19 and AIDS.",
    "knowledge/books/usury-a-scriptual-ethic-and-economic.md": "Notes on John T. Noonan Jr.'s history of the Christian prohibition on usury — its scriptural basis, its enforcement across centuries, and its gradual dissolution.",
    "knowledge/books/woke-inc.md": "Notes on Vivek Ramaswamy's argument that corporate social justice commitments function as a shield for concentrated economic power rather than genuine moral progress.",
    "knowledge/characters/kathryn-merteuil.md": "Character study of Kathryn Merteuil from Cruel Intentions — her manipulation tactics, her power architecture, and what she reveals about predatory social performance.",
    "knowledge/characters/quick-ben.md": "Character study of Quick Ben from the Malazan Book of the Fallen — his power, his secrecy, his loyalty to Kalam, and the philosophical weight the series places on deliberate concealment.",
    "knowledge/concepts/azt.md": "Reference entry on AZT (zidovudine) — its development as a cancer drug, its fast-tracked approval for AIDS, and the controversies over toxicity, dosing, and the clinical evidence base.",
    "knowledge/concepts/cia-influence-operations-operation-mockingbird.md": "Reference entry on CIA domestic and foreign influence operations, with focus on Operation Mockingbird — the alleged program to place agency assets inside major media organizations.",
    "knowledge/concepts/citizens-united.md": "Reference entry on stakeholder capitalism — the model arguing corporations owe obligations to employees, communities, and society, not only shareholders.",
    "knowledge/concepts/cointelpro.md": "Reference entry on COINTELPRO — the FBI's covert domestic counterintelligence program targeting civil rights groups, socialist organizations, and political dissidents from the 1950s through 1971.",
    "knowledge/concepts/esg-scores.md": "Reference entry on ESG scoring as a governance mechanism — how environmental, social, and governance ratings function as soft regulatory infrastructure outside the democratic process.",
    "knowledge/concepts/fifth-generation-warfare.md": "Reference entry on fifth-generation warfare — conflict conducted through information, perception, culture, and institutional manipulation rather than conventional military force.",
    "knowledge/concepts/grand-strategy.md": "Reference entry on grand strategy — the long-horizon coordination of military, economic, diplomatic, and informational power toward durable national or imperial objectives.",
    "knowledge/concepts/israeli-connection.md": "Reference entry on the documented relationships between Israel, pro-Israel donor networks, and the TPUSA ecosystem — speakers, funding, and policy alignment.",
    "knowledge/concepts/mandrake-mechanism.md": "Reference entry on the Mandrake Mechanism — G. Edward Griffin's description of how the Federal Reserve creates money from debt, as argued in The Creature from Jekyll Island.",
    "knowledge/concepts/mk-ultra.md": "Reference entry on MK-Ultra — the CIA's covert human experimentation program using LSD, hypnosis, and psychological torture to research mind control from 1953 to 1973.",
    "knowledge/concepts/mrna.md": "Reference entry on mRNA vaccine technology, with focus on Bret Weinstein's critique — the spike protein as a systemic toxin, immune imprinting, and the case for scrutinizing long-term effects.",
    "knowledge/concepts/operation-gladio.md": "Reference entry on Operation Gladio — the NATO-sponsored stay-behind network in postwar Europe, its links to terrorism, and what it demonstrates about covert state violence.",
    "knowledge/concepts/osmotic-pressure.md": "Reference entry on osmotic pressure in biology and social systems — how concentration gradients drive movement and how the metaphor applies to migration and demographic pressure.",
    "knowledge/concepts/pinocchio-state.md": "Reference entry on Michael Yon's Pinocchio State framework — the lifecycle of a proxy or puppet state from creation through use to disposal, mapped against US unconventional warfare doctrine.",
    "knowledge/concepts/project-bluebird.md": "Reference entry on Project BLUEBIRD — the early CIA mind-control research program that preceded Artichoke and MK-Ultra, focused on hypnotic interrogation and behavior modification.",
    "knowledge/concepts/regulation.md": "Reference entry on regulation as a political economy phenomenon — how rules get written, who shapes them, and the structural tendency for industries to capture their own regulators.",
    "knowledge/concepts/regulatory-capture.md": "Reference entry on regulatory capture — the process by which the agencies meant to regulate an industry come to serve that industry's interests instead of the public's.",
    "knowledge/concepts/richard-werner-economics.md": "Reference entry on Richard Werner's credit-centric economic framework — his quantity theory of credit, his critique of central banking, and how his work relates to Austrian, Keynesian, and Post-Keynesian traditions.",
    "knowledge/concepts/romanian-angels.md": "Reference entry on the Romanian orphan crisis and the AIDS epidemic among institutionalized children — the medical and political failures that allowed mass HIV transmission.",
    "knowledge/concepts/rothbard/austrian-business-cycle-theory.md": "Reference entry on Austrian Business Cycle Theory as formulated by Mises and Rothbard — how artificially low interest rates create malinvestment booms that inevitably collapse.",
    "knowledge/concepts/rothbard/fractional-reserve.md": "Reference entry on fractional reserve banking — how banks create money through lending, the multiplication effect, and Rothbard's argument that the practice constitutes fraud.",
    "knowledge/concepts/rothbard/sound-money.md": "Reference entry on sound money as defined by the Austrian tradition — commodity-backed currency, the gold standard, and the case against central bank discretion over money supply.",
    "knowledge/concepts/rothbard/time-preference.md": "Reference entry on time preference in Austrian economics — the universal human tendency to value present goods over future goods, and its implications for interest rates and capital formation.",
    "knowledge/concepts/rothchild-family.md": "Reference entry on the Rothschild banking dynasty — its origins in Frankfurt, its role in financing European wars and governments, and its place in contemporary political mythology.",
    "knowledge/concepts/rothchild-formula.md": "Reference entry on the Rothschild Formula as described by G. Edward Griffin — the alleged strategy of financing multiple sides of conflicts to profit from war and expand financial control.",
    "knowledge/concepts/shaped-charge-theory.md": "Reference entry on shaped charge ballistics — the physics of directional explosive energy, its forensic implications, and how it applies to contested wound analysis in the Charlie Kirk shooting case.",
    "knowledge/concepts/shareholder-capitalism.md": "Reference entry on shareholder primacy capitalism — the Milton Friedman doctrine that corporations exist to maximize returns to shareholders, and the critiques it has attracted.",
    "knowledge/concepts/thimerosal.md": "Reference entry on thimerosal — the mercury-based vaccine preservative, the controversy over its alleged link to autism, the studies used to dismiss that link, and the critics who dispute those studies.",
    "knowledge/concepts/transnational-capital.md": "Reference entry on transnational capitalism — the theory that a global capitalist class has emerged whose interests are no longer tied to any single nation-state.",
    "knowledge/concepts/usury.md": "Reference entry on usury — the historical prohibition on interest-bearing loans in Christianity and Islam, its theological basis, and its gradual disappearance as capitalism developed.",
    "knowledge/concepts/vioxx.md": "Reference entry on Vioxx (rofecoxib) — the Merck painkiller withdrawn in 2004 after cardiovascular deaths, the suppressed trial data, and what it demonstrates about pharmaceutical regulatory failure.",
    "knowledge/concepts/wokeism.md": "Reference entry on wokeism as a political and cultural phenomenon — its origins in social justice activism, its institutionalization in corporations and universities, and the backlash it generated.",
    "knowledge/concepts/world-revolutions.md": "Reference entry on Nesta Webster's World Revolution thesis — her argument that a continuous revolutionary conspiracy has driven Western upheaval since the Illuminati, and the scholarly context for evaluating it.",
    "knowledge/concepts/zionism/political-zionism.md": "Reference entry on political Zionism — Herzl's founding argument, the movement's early factions, and the distinction between political, cultural, and religious Zionism.",
    "knowledge/concepts/zionism/zionism.md": "Reference entry on Zionism as a political movement — its history from the 1890s through the founding of Israel, its internal divisions, and the debates it continues to generate.",
    "knowledge/events/aids-crisis.md": "Entry on the AIDS dissident movement — the scientists and physicians who challenged the HIV-causes-AIDS consensus, their arguments, and how the mainstream medical community responded.",
    "knowledge/events/aspen-donor-retreat.md": "Entry on the August 2025 Aspen donor retreat — what is known about who attended, what was discussed, and its significance as a node in elite conservative donor coordination.",
    "knowledge/events/bolshevik-revolution.md": "Entry on the Bolshevik Revolution of 1917 — the political conditions, the financing question, and the long-running debate over Western banking interests and the revolution's backing.",
    "knowledge/events/charlie-kirk-shooting.md": "Entry on the Charlie Kirk shooting incident — the known facts, the contested evidence, and the investigative threads connecting the event to the broader TPUSA research.",
    "knowledge/events/covid-censorship.md": "Entry on the censorship-industrial complex — the documented coordination between federal agencies, social media platforms, and NGOs to suppress COVID-19 dissent.",
    "knowledge/events/crime-scene-paving.md": "Entry on the paving of the UVU crime scene — the timeline, what was destroyed, the official explanations, and why critics argue it compromised the shooting investigation.",
    "knowledge/events/spanish-inquisition.md": "Entry on Joseph de Maistre's defense of the Spanish Inquisition — his argument for institutional religious authority, his political theology, and what it reveals about reactionary thought.",
    "knowledge/events/tpusa-doge-audit.md": "Pointer entry on the TPUSA DOGE audit — the Department of Government Efficiency inquiry into TPUSA's federal funding and the public documents it produced.",
    "knowledge/evidence/atf-report-and-forensic-findings.md": "Evidence entry summarizing the ATF report and forensic findings from the Charlie Kirk shooting — ballistics, weapon identification, and the contested conclusions.",
    "knowledge/evidence/ballistics.md": "Evidence entry on the ballistics dispute in the Charlie Kirk shooting — why the .30-06 wound trajectory is physically contested and what that implies for competing shooting scenarios.",
    "knowledge/evidence/charlie-kirk-necklace.md": "Evidence entry on Charlie Kirk's necklace as a research reference — what the jewelry shows in various photographs, and why researchers treat it as a potential chronological marker.",
    "knowledge/evidence/text-messages.md": "Evidence entry on the Robinson-Twiggs text message exchange — what the messages show, their context, and how they are used in arguments about foreknowledge or coordination.",
    "knowledge/games/myst.md": "A close reading of Myst (1993) as philosophical fiction — its epistemology of testimony, its treatment of authorship and consequence, and its analogy for arriving in a world you did not build.",
    "knowledge/hypotheses/why-clinical-shift-in-60s.md": "Hypothesis on why clinical psychiatry shifted from treating neuroses to character disorders in the 1960s — the role of institutional decay, pharmaceutical incentives, and cultural narcissism.",
    "knowledge/organizations/fabian-society.md": "Reference entry on the Fabian Society — the British socialist organization that advocated for gradual, institutional reform over revolution, and its long influence on Labour politics.",
    "knowledge/organizations/federal-reserve.md": "Reference entry on the Federal Reserve System — its founding at Jekyll Island, its structure as a hybrid public-private institution, and the Austrian and populist critiques of its operation.",
    "knowledge/organizations/project-of-the-new-american-century.md": "Reference entry on PNAC — the neoconservative think tank whose 2000 manifesto called for U.S. military dominance and whose signatories shaped the post-9/11 foreign policy agenda.",
    "knowledge/organizations/the-bank-of-england.md": "Reference entry on the Bank of England — its founding in 1694, its role in financing British wars, and its place in the history of central banking and monetary control.",
    "knowledge/organizations/tpusa-faith.md": "Reference entry on TPUSA Faith — the religious outreach arm of Turning Point USA, its leadership, its donor connections, and its role in the broader TPUSA ecosystem.",
    "knowledge/organizations/turning-point-usa.md": "Reference entry on Turning Point USA — its founding, funding sources, leadership structure, controversies, and its function in the conservative campus and media ecosystem.",
    "knowledge/organizations/unification-church.md": "Reference entry on the Unification Church (Moon Inc.) — Sun Myung Moon's organization, its media holdings, its political relationships, and its connections to conservative movement infrastructure.",
    "knowledge/organizations/usaid.md": "Reference entry on USAID in Afghanistan — the agency's role in reconstruction, the documented waste and fraud, and the SIGAR findings on what the money actually built.",
    "knowledge/people/andrew-kolvet.md": "Profile of Andrew Kolvet — Charlie Kirk's chief of staff, his background, his relationships with key donors and political figures, and his role in TPUSA's internal operations.",
    "knowledge/people/anthony-fauci.md": "Profile of Anthony Fauci — his tenure at NIAID, his management of HIV/AIDS and COVID-19 research, his relationships with pharmaceutical partners, and the case made against him by critics.",
    "knowledge/people/baron-coleman.md": "Profile of Baron Coleman — the investigator and commentator whose research into the Charlie Kirk shooting and TPUSA has been a primary source for the investigative thread.",
    "knowledge/people/blake-neff.md": "Profile of Blake Neff — Tucker Carlson's head writer, his departure following exposure of his online racist posts, and what his case reveals about Fox News's content operation.",
    "knowledge/people/bret-weinstein.md": "Profile of Bret Weinstein — evolutionary biologist, Dark Horse podcast host, his COVID heterodoxy, and his arguments about vaccine safety, institutional capture, and evolutionary medicine.",
    "knowledge/people/candace-owens.md": "Profile of Candace Owens — her trajectory from liberal blogger to TPUSA figurehead to independent commentator, and her departure from the mainstream conservative ecosystem.",
    "knowledge/people/charlie-kirk-information-environment.md": "Analysis of the information environment surrounding Charlie Kirk — the psychological operations framing, the media ecosystem, and the sources shaping public perception of him.",
    "knowledge/people/charlie-kirk.md": "Profile of Charlie Kirk — TPUSA founder, his rise in conservative media, key relationships, financial controversies, and the investigative threads connecting him to the shooting case.",
    "knowledge/people/erika-kirk.md": "Profile of Erika Kirk (née Frantzve) — Charlie Kirk's wife, her background, her Israel trip, the circumstances of their meeting, and the interpretive theories around her role.",
    "knowledge/people/erika-kirk/behavioral-patterns.md": "Analysis of behavioral patterns attributed to Erika Kirk — recurring behaviors documented across sources and their significance to the broader investigative framework.",
    "knowledge/people/lori-frantzve.md": "Profile of Lori Frantzve — Erika Kirk's mother, her background, her documented relationships, and her role in the investigative thread around the Kirk family.",
    "knowledge/people/nesta-helen-webster.md": "Profile of Nesta Helen Webster — the early 20th-century British conspiracy theorist whose World Revolution thesis shaped modern anti-globalist and anti-Semitic narratives.",
    "knowledge/people/robert-f-kennedy-jr.md": "Profile of Robert F. Kennedy Jr. — his environmental law career, his vaccine safety advocacy, his 2024 presidential run, and his appointment as HHS Secretary.",
    "knowledge/people/tyler-bowyer.md": "Profile of Tyler Bowyer — TPUSA's chief operating officer, his political background, and his role in Arizona Republican Party operations.",
    "knowledge/people/tyler-robinson.md": "Profile of Tyler Robinson — a figure connected to the Charlie Kirk shooting investigation, his documented relationships, and his significance to the evidence record.",
    "knowledge/projects/greater-israel-project.md": "Reference entry on the Greater Israel Project thesis — its origins in Oded Yinon's 1982 strategy paper, its popularization by Michel Chossudovsky, and an assessment of the evidence for and against it.",
    "knowledge/research/bret-weinstein/2026-08-01-darien-gap-migration-and-china-hypothesis.md": "Research notes on Bret Weinstein's hypothesis that China has deliberately facilitated migration through the Darién Gap as a form of asymmetric warfare against the United States.",
    "knowledge/research/chris-martenson/2024-01-27-darien-gap-kim-iverson.md": "Research notes on Chris Martenson's discussion with Kim Iversen about the Darién Gap migration pipeline — the infrastructure, the facilitation networks, and the geopolitical implications.",
    "knowledge/research/chris-martenson/2026-08-01-energy-shock-oil-markets-and-inflation.md": "Research notes on Chris Martenson's analysis of how the Iran war, oil futures manipulation, and refinery constraints are feeding into broader inflation dynamics.",
    "knowledge/research/chris-martenson/2026-08-03-gold-discussion.md": "Research notes on Chris Martenson's discussion of gold's role in the slow unwinding of the dollar-based monetary system and the migration of gold reserves from West to East.",
    "knowledge/research/chris-martenson/2026-08-03-oil-discussion.md": "Research notes on Chris Martenson's argument that oil markets are subject to price setting rather than price discovery — and what that means for stagflation.",
    "knowledge/research/chris-martenson/2026-08-04-talk-with-multipolarity.md": "Research notes on Chris Martenson's conversation about oil market manipulation, geopolitics, and the structural forces driving energy-sector instability.",
    "knowledge/research/chris-martenson/2026-08-16-inflation-illusion.md": "Research notes on Chris Martenson's analysis of why official inflation measures understate the cost-of-living increases most Americans are experiencing.",
    "knowledge/research/dave-decamp/2026-08-03-lock-and-loaded.md": "Research notes on Dave DeCamp's reporting on a week of American war activity — the near-strikes, the standing-downs, and the pattern of escalation management in the Middle East.",
    "knowledge/research/dave-decamp/2026-08-05-updates.md": "Research notes on Dave DeCamp's updates on the US military footprint in Somalia and simmering tensions involving Iran, Gaza, and Lebanon.",
    "knowledge/research/jay-martin/2026-08-16-japans-bailout.md": "Research notes on the U.S. currency intervention to support the Japanese yen — why it happened, who authorized it, and what it reveals about dollar system management.",
    "knowledge/research/jiang-xueqin/2026-07-01-emergency-podcast.md": "Research notes on Jiang Xueqin's emergency discussion of the Ceuta migrant crossing — the event, its geopolitical framing, and Jiang's broader argument about migration as warfare.",
    "knowledge/research/jiang-xueqin/2026-08-17-jiang.md": "Research notes on Jiang Xueqin's eschatological reading of the Iran war — his argument that the conflict is not primarily about land or resources but about End Times theology.",
    "knowledge/research/jiang-xueqin/religion-and-capital.md": "Research notes on Jiang Xueqin's analysis of the relationship between religious motivation and capital formation — how belief systems shape economic behavior and elite coordination.",
    "knowledge/research/macroeconomics/strait-of-hormuz-energy-shock.md": "Research notes on the Strait of Hormuz as an energy chokepoint — the scenarios for an oil supply shock and the inflation and debt dynamics that would follow.",
    "knowledge/research/macroeconomics/us-debt-trap-rising-yields.md": "Research notes on the US debt trap — how rising Treasury yields interact with deficit spending to create a potential debt spiral with 1970s-style parallels.",
    "knowledge/research/michael-yon/2025-09-08-darien-gap-routes-and-resources.md": "Research notes on Michael Yon's reporting on Darién Gap migration routes — the infrastructure, the nationalities moving through, and the resource geography of the crossing.",
    "knowledge/research/michael-yon/2026-04-19-suez-pinnocio.md": "Research notes on Michael Yon's Suez-Pinocchio framework — his argument mapping the Pinocchio State lifecycle onto Israel's strategic position relative to US foreign policy.",
    "knowledge/research/michael-yon/2026-05-17-financial-rebellion-interview.md": "Research notes on Michael Yon's discussion of US-China trade war dynamics, strategic chokepoints, and the broader economic warfare dimension of the conflict.",
    "knowledge/research/michael-yon/2026-06-11-drug-babies.md": "Research notes on Michael Yon's discussion of drug babies, patent medicines, media criticism, and his argument that war continuation serves pharmaceutical and media interests.",
    "knowledge/research/michael-yon/2026-06-20-baby-refuge.md": "Research notes on Michael Yon's reporting on birth refugees, the midwifery movement, and the medical distrust driving some Americans to seek alternative birth settings.",
    "knowledge/research/michael-yon/2026-07-26-mario-nafal-interview.md": "Research notes on Michael Yon's interview with Mario Nafal — his geopolitical framework, predictions, and analysis of active conflict zones.",
    "knowledge/research/michael-yon/2026-07-30-war-growing-discussion.md": "Research notes on Michael Yon's worldview and depopulation framework — his claim that elite actors are deliberately engineering population reduction through war, famine, and medical intervention.",
    "knowledge/research/michael-yon/2026-07-31-morocco-ceuta-and-resource-geography.md": "Research notes on Michael Yon's analysis of Morocco, the Ceuta enclave, and the resource geography driving North African migration pressure toward Europe.",
    "knowledge/research/michael-yon/2026-08-02-war-churches.md": "Research notes on Michael Yon's argument about military service, custodial parents, memory, and his prediction of an approaching draft.",
    "knowledge/research/michael-yon/michael-yon-prediction-tracker.md": "A running tracker of Michael Yon's specific predictions — what he has said, when, and whether subsequent events confirmed, contradicted, or left his claims unresolved.",
    "knowledge/research/mises/economic-calculation.md": "Reference notes on Mises's economic calculation argument — the claim that rational economic planning is impossible without price signals, and what it implies for socialism.",
    "knowledge/research/mises/praxeology.md": "Reference notes on praxeology — Mises's framework for economics as the science of human action, deduced from the axiom of purposeful behavior rather than empirical observation.",
    "knowledge/research/peter-mccullough/2026-08-16-mrna-harms.md": "Research notes on the IgG4 hypothesis — the proposed mechanism linking repeated mRNA exposure to antibody class switching toward a tolerizing response and potential chronic immune dysregulation.",
    "knowledge/research/salatin/everything-i-want-to-do-is-illegal.md": "Research notes on Joel Salatin's argument that federal and state regulations systematically prevent small-scale farmers from raising, processing, and selling food on their own terms.",
    "knowledge/research/scott-horton/2026-08-09-understanding-the-fed.md": "Research notes on Scott Horton's discussion with Robert Murphy on the Federal Reserve, fractional reserve banking, the business cycle, and where the current economy stands.",
    "knowledge/research/scott-horton/2026-08-10-glenn-greenwald.md": "Research notes on Scott Horton's conversation with Glenn Greenwald about the political realignment — how foreign policy, civil liberties, and media captured has reshuffled old coalitions.",
    "knowledge/research/scott-horton/2026-08-16-next-bin-laden.md": "Research notes on Scott Horton's analysis of how the Gaza war and Iran escalation are generating the conditions for the next generation of anti-American terrorism.",
    "knowledge/research/scott-horton/2026-08-17-blowback.md": "Research notes on Scott Horton's blowback framework — how US interventions in the Middle East predictably create the adversaries they claim to be fighting.",
    "knowledge/research/sigar-testimonial-afghanistan.md": "Reference notes on SIGAR Inspector General John Sopko's April 2023 congressional testimony — the documented failures of US reconstruction in Afghanistan and the systemic reasons for them.",
    "knowledge/research/thomas-sowell/perspectives-on-blm.md": "Research notes on Thomas Sowell's arguments about welfare dependency, the black family, and his critique of social justice frameworks that he argues cause the harms they claim to fix.",
    "knowledge/research/yaakov-shapiro/2026-08-03-israel-is-not-judism.md": "Research notes on Rabbi Yaakov Shapiro's argument that Zionism and Judaism are fundamentally incompatible — the halachic basis, the Satmar tradition, and the institutional size of Orthodox anti-Zionism.",
    "knowledge/research/yaakov-shapiro/2026-08-03-last-of-his-species.md": "Research notes on Rabbi Yaakov Shapiro's account of the Satmar Rebbe — his theology, his opposition to Zionism, and his claim to represent a disappearing tradition of principled Jewish separatism.",
    "knowledge/syntheses/austrian-economics-analysis-of-2020s.md": "Cross-source synthesis applying Mises, Hayek, and Rothbard's frameworks to 2020s economic events — the COVID money printing, the inflation surge, and the boom-bust cycle dynamics.",
    "knowledge/syntheses/elliot-vs-griffin-on-banks-in-america.md": "Cross-source synthesis comparing J.H. Elliott's and G. Edward Griffin's accounts of central banking in America — the First and Second Banks of the United States and the political fights over them.",
    "knowledge/syntheses/financing-both-sides.md": "Cross-source synthesis on the documented pattern of financing multiple sides of conflicts — from the Rothschild formula to modern defense contractor relationships.",
    "knowledge/syntheses/lasch-austrian-time-preference.md": "Cross-source synthesis connecting Christopher Lasch's cultural critique of narcissism to the Austrian economics concept of time preference — how monetary instability compresses long-horizon thinking.",
    "knowledge/syntheses/what-caused-the-shift-from-neurosis-to-character-disorder.md": "Cross-source synthesis examining the shift in psychiatric presentation from classical neuroses to diffuse character disorders — institutional, pharmaceutical, and cultural explanations.",
    "knowledge/wars/afghanistan/afghanistan-wars.md": "Entry on the wars in Afghanistan from 1979 to 2021 — the Soviet invasion, the CIA's proxy war, the Taliban's rise, the US occupation, and the documented failures of nation-building.",
    "knowledge/wars/planning/clean-break-strategy.md": "Entry on A Clean Break (1996) — the neoconservative strategy paper written for Netanyahu advocating regime change in Iraq and Syria as part of Israeli security doctrine.",
    "knowledge/wars/planning/seven-countries-five-years.md": "Entry on General Wesley Clark's account of the post-9/11 Pentagon memo listing seven countries for regime change — its authenticity, its implications, and how subsequent events tracked against it.",
}


def add_description(filepath, description):
    with open(filepath, 'r') as f:
        content = f.read()

    if 'description:' in content:
        print(f"SKIP (already has description): {filepath}")
        return

    # Insert after the last front-matter field before closing ---
    # Find the closing --- of front matter
    # Front matter is between first and second ---
    parts = content.split('---', 2)
    if len(parts) < 3:
        print(f"SKIP (no front matter): {filepath}")
        return

    front = parts[1]
    body = parts[2]
    # Add description at end of front matter block
    front = front.rstrip('\n') + f'\ndescription: "{description}"\n'
    new_content = f'---{front}---{body}'

    with open(filepath, 'w') as f:
        f.write(new_content)
    print(f"OK: {filepath}")


for path, desc in DESCRIPTIONS.items():
    if os.path.exists(path):
        add_description(path, desc)
    else:
        print(f"NOT FOUND: {path}")
