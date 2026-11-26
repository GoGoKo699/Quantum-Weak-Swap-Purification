# Project understanding map

This route gives 30 milestones for weak-SWAP purification. The first 12 build the quantum and statistical setting. The last 18 follow one operation through the proof of its sample cost, then relate it to the measure-and-prepare benchmark. The [Watrous bridge](WATROUS_BRIDGE.md) maps the relevant parts of the single educational anchor, and the [tutorial](TUTORIAL.md) gives a complete worked first step.

| Milestones | Connection |
|---|---|
| [M01](#m01-target-states-and-density-operators)–[M04](#m04-independent-arrivals-and-tensor-factors) | States, noise, accuracy and independent arrivals |
| [M05](#m05-discarding-a-register)–[M09](#m09-common-basis-covariance) | Reduction, heralding, coherent control and covariance |
| [M10](#m10-expectation-with-restarts)–[M12](#m12-the-streaming-task) | Restart costs, uniform moments and the operational model |
| [M13](#m13-the-weak-swap-circuit)–[M18](#m18-acceptance-after-sector-measurement) | The weak operation and the ceiling of sector projection |
| [M19](#m19-scheduling-a-positive-gain)–[M23](#m23-exact-renewal-accounting) | The schedule, a worked step and exact copy accounting |
| [M24](#m24-the-inverse-infidelity-cost-law)–[M25](#m25-source-quality-and-dimension) | Asymptotic cost and its dependence on dimension |
| [M26](#m26-output-from-a-classical-record)–[M30](#m30-the-complete-scientific-result) | The comparison, finite evidence and the full result |

## Background and preliminaries

### M01 Target states and density operators

**Central question.** What does it mean to receive a noisy quantum state?

**Understanding target.** Represent a pure target by a rank-one projector and a mixed input by a positive trace-one operator. The target direction is a physical parameter shared by the preparations.

**Prerequisites.** None.

**Conceptual connection.** The trace with the target projector is a measurable population if that projector is known.

**Sources.** [Model](../science/model.md). Watrous §§2.1.2–2.1.3 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M02 Depolarized input copies

**Central question.** What does the known input noise tell you when the target is unknown?

**Understanding target.** Write the fresh state as a mixture of the target and the uniform state. Determine the target population from the signal weight and dimension while leaving the target direction unspecified.

**Prerequisites.** [M01](#m01-target-states-and-density-operators).

**Conceptual connection.** The shared spectrum gives the controller a scalar starting value without a directional reference.

**Sources.** [Model](../science/model.md). Watrous §§2.1.2 and 2.2.3 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M03 Output overlap

**Central question.** How is a released state judged?

**Understanding target.** Use its population along the pure target to define fidelity and the remaining weight to define infidelity. Distinguish the required overlap from purity, which can increase even for a state pointing away from the target.

**Prerequisites.** [M01](#m01-target-states-and-density-operators), [M02](#m02-depolarized-input-copies).

**Conceptual connection.** The accuracy threshold is imposed on the released state and the controller tracks the same scalar throughout the accepted sequence.

**Sources.** [Model](../science/model.md). Watrous §3.2.1 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M04 Independent arrivals and tensor factors

**Central question.** How do separate copies combine mathematically?

**Understanding target.** Use a product state for independent arrivals conditional on the shared target. Name the retained, incoming and control tensor factors by their different physical roles.

**Prerequisites.** [M01](#m01-target-states-and-density-operators), [M02](#m02-depolarized-input-copies).

**Conceptual connection.** The product form is what makes the exact SWAP calculation possible in each successful round.

**Sources.** [Model](../science/model.md). Watrous §§1.1.2 and 2.1.2 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M05 Discarding a register

**Central question.** What remains after one register leaves the apparatus?

**Understanding target.** Compute the retained state using the partial trace and understand why discarding is a quantum channel. Keep track of the trace when the joint state already represents a selected branch.

**Prerequisites.** [M01](#m01-target-states-and-density-operators), [M04](#m04-independent-arrivals-and-tensor-factors).

**Conceptual connection.** This reduction turns an operation on two data systems into an update for the single system kept across arrivals.

**Sources.** [Weak-SWAP operation](../science/weak-swap.md). Watrous §§2.1.3 and 2.2.3 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M06 Measurement effects and branches

**Central question.** What information does a herald convey?

**Understanding target.** Separate the measurement effect that gives a probability from the completely positive map that gives an unnormalized retained state. Divide by the branch trace to obtain the conditional state.

**Prerequisites.** [M03](#m03-output-overlap), [M05](#m05-discarding-a-register).

**Conceptual connection.** One bit of measurement output can specify a useful conditional quantum state without identifying the target direction.

**Sources.** [Weak-SWAP operation](../science/weak-swap.md). Watrous §§2.2.1–2.2.2 and 2.3.1–2.3.2 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M07 SWAP and its two sectors

**Central question.** Why can two copies be compared without a target basis?

**Understanding target.** Describe SWAP as a unitary permutation with eigenvalues plus and minus one. Recover the two sector projectors by adding or subtracting SWAP from the identity and dividing by two.

**Prerequisites.** [M04](#m04-independent-arrivals-and-tensor-factors).

**Conceptual connection.** The same permutation compares the contents of the registers in every common basis.

**Sources.** [Weak-SWAP operation](../science/weak-swap.md). Watrous §7.1.1 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M08 Coherent control before measurement

**Central question.** How do two controlled alternatives interfere?

**Understanding target.** Explain how undoing the preparation of a control qubit adds amplitudes for a selected outcome. A measured sector label would instead distinguish the alternatives and remove their interference.

**Prerequisites.** [M06](#m06-measurement-effects-and-branches), [M07](#m07-swap-and-its-two-sectors).

**Conceptual connection.** The outcome branch can preserve part of both SWAP eigenspaces and preserve cross terms between them.

**Sources.** [Weak-SWAP operation](../science/weak-swap.md). Watrous §§2.2.2 and 2.3.1–2.3.2 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M09 Common-basis covariance

**Central question.** Why is the analysis allowed to put the target along one basis vector?

**Understanding target.** Show that SWAP commutes with applying the same unitary to both data registers. Express the connection between rotating the inputs and rotating the conditional output.

**Prerequisites.** [M04](#m04-independent-arrivals-and-tensor-factors), [M07](#m07-swap-and-its-two-sectors), [M08](#m08-coherent-control-before-measurement).

**Conceptual connection.** A calculation in one target basis then proves the same overlap update for every target direction.

**Sources.** [Weak-SWAP operation](../science/weak-swap.md). Watrous §§2.2.1 and 7.1.1 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M10 Expectation with restarts

**Central question.** What does a failure cost?

**Understanding target.** Compute an expected cost from the first attempt and the work repeated after failure. Include the incoming sample consumed during a failed step.

**Prerequisites.** [M06](#m06-measurement-effects-and-branches).

**Conceptual connection.** Renewal charges the raw input spent retrieving the current stage as well as the final rejected sample.

**Sources.** [Sample cost](../science/sample-cost.md). Watrous §1.2.2 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M11 Uniform state averages

**Central question.** What operator represents a uniformly drawn pure-state ensemble?

**Understanding target.** Relate the uniform moment of repeated pure projectors to the normalized projector onto the symmetric subspace. Identify the dimension ratio between the symmetric spaces of adjacent copy counts.

**Prerequisites.** [M04](#m04-independent-arrivals-and-tensor-factors), [M07](#m07-swap-and-its-two-sectors).

**Conceptual connection.** This supplies a fidelity bound that applies separately to every terminal measurement effect.

**Sources.** [Measure-and-prepare benchmark](../science/measure-prepare.md). Watrous §§7.1.1 and 7.2.1–7.2.2 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M12 The streaming task

**Central question.** Which parts of the experiment may persist and which parts are charged?

**Understanding target.** Bring together the source promise, output overlap, classical herald, persistent register and transient registers. Distinguish the expected number of input copies from space held coherently between arrivals.

**Prerequisites.** [M02](#m02-depolarized-input-copies), [M03](#m03-output-overlap), [M06](#m06-measurement-effects-and-branches), [M09](#m09-common-basis-covariance), [M10](#m10-expectation-with-restarts), [M11](#m11-uniform-state-averages).

**Conceptual connection.** The full model states what it would mean to gain fidelity with one retained register and how to compare the result with classical-record output.

**Sources.** [Model](../science/model.md) · [verification guide](../verification/README.md). Watrous §§2.1–2.3 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

## Scientific narrative

### M13 The weak-SWAP circuit

**Central question.** How does the successful branch implement a tunable filter?

**Understanding target.** Compute the success operator by following control preparation, controlled SWAP and the selected measurement outcome. Verify that the symmetric amplitude stays fixed and the antisymmetric amplitude changes with the control strength.

**Prerequisites.** [M06](#m06-measurement-effects-and-branches), [M07](#m07-swap-and-its-two-sectors), [M08](#m08-coherent-control-before-measurement), [M12](#m12-the-streaming-task).

**Conceptual connection.** The explicit operation uses one stored data register, one incoming register and one control qubit.

**Sources.** [Weak-SWAP operation](../science/weak-swap.md). Watrous §§2.2.2 and 2.3.1–2.3.2 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M14 The unnormalized retained state

**Central question.** Which terms survive after the input register is discarded?

**Understanding target.** Expand the success operator on both sides of the product state. Identify the original state terms and both operator products from the identity–SWAP cross terms.

**Prerequisites.** [M04](#m04-independent-arrivals-and-tensor-factors), [M05](#m05-discarding-a-register), [M13](#m13-the-weak-swap-circuit).

**Conceptual connection.** Taking the trace gives the probability of the herald, and taking the target population gives the normalization numerator.

**Sources.** [Weak-SWAP operation](../science/weak-swap.md). Watrous §§1.1.2 and 2.1.3 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M15 Closure on one scalar

**Central question.** Why does a single number describe the retained output after success?

**Understanding target.** Use the common target eigenspace and uniform orthogonal population to see that the success branch stays in the depolarized family. Track the new target population instead of a direction or a density matrix.

**Prerequisites.** [M02](#m02-depolarized-input-copies), [M09](#m09-common-basis-covariance), [M14](#m14-the-unnormalized-retained-state).

**Conceptual connection.** The controller can schedule all subsequent strengths from the known source quality and its success count.

**Sources.** [Weak-SWAP operation](../science/weak-swap.md). Watrous §§2.1.2 and 7.1.1 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M16 Gain and replacement loss

**Central question.** Why can the same interaction help or harm a high-quality retained state?

**Understanding target.** Separate the gain proportional to the identity–SWAP interference from the term that replaces part of the retained state with a fresh, noisier state. Read the resulting sign condition on the filter strength.

**Prerequisites.** [M03](#m03-output-overlap), [M14](#m14-the-unnormalized-retained-state), [M15](#m15-closure-on-one-scalar).

**Conceptual connection.** This tradeoff determines how the interaction must weaken near the output target.

**Sources.** [Weak-SWAP operation](../science/weak-swap.md). Watrous §§2.1.3 and 2.2.2 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M17 Ceiling of strong symmetric projection

**Central question.** Why does repeating a strong test stop helping?

**Understanding target.** Analyze the fixed point of the target-population update at full symmetric projection. Explain why directly combining a stored high-quality state with a fixed raw-quality source yields a ceiling below perfect fidelity.

**Prerequisites.** [M07](#m07-swap-and-its-two-sectors), [M15](#m15-closure-on-one-scalar), [M16](#m16-gain-and-replacement-loss).

**Conceptual connection.** A fixed strong filter becomes a useful baseline for isolating the effect of an adaptive weak filter.

**Sources.** [Weak-SWAP operation](../science/weak-swap.md) · [literature comparisons](../references/RELATED_WORK.md). Watrous §7.1.1 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M18 Acceptance after sector measurement

**Central question.** Can a randomized acceptance rule substitute for coherent attenuation?

**Understanding target.** Compare the normalized outputs from the two measured sectors. See that reweighting their measured probabilities gives a mixture bounded by the better sector output in this model.

**Prerequisites.** [M06](#m06-measurement-effects-and-branches), [M08](#m08-coherent-control-before-measurement), [M14](#m14-the-unnormalized-retained-state), [M17](#m17-ceiling-of-strong-symmetric-projection).

**Conceptual connection.** The unequal-purity steps rely on cross-sector coherence, which changing the acceptance probabilities after the measurement cannot restore.

**Sources.** [Weak-SWAP operation](../science/weak-swap.md). Watrous §§2.3.1–2.3.2 and 7.1.1 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M19 Scheduling a positive gain

**Central question.** How can the filter power be set without estimating the target direction?

**Understanding target.** Use the current scalar overlap to choose a fixed fraction of the strength that would give zero gain. Verify that the positive increment and the eventual approach to fidelity one follow from this schedule.

**Prerequisites.** [M12](#m12-the-streaming-task), [M15](#m15-closure-on-one-scalar), [M16](#m16-gain-and-replacement-loss), [M18](#m18-acceptance-after-sector-measurement).

**Conceptual connection.** A single sequence of known scalar controls can turn the local gain into a streaming procedure.

**Sources.** [Sample cost](../science/sample-cost.md). Watrous §§2.2.1–2.2.2 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M20 A complete one-step example

**Central question.** What does the first herald buy in a qubit example?

**Understanding target.** For signal weight 0.8, identify the 0.9 starting overlap, compute the probability of the first success, and interpret the conditional output overlap and the average number of inputs used to reach it.

**Prerequisites.** [M13](#m13-the-weak-swap-circuit), [M14](#m14-the-unnormalized-retained-state), [M19](#m19-scheduling-a-positive-gain).

**Conceptual connection.** The first step uses equal-quality inputs. Later steps enter the unequal-input regime where the memory's quality changes the choice of control.

**Sources.** [Worked tutorial](TUTORIAL.md#work-through-the-first-step). Watrous §§1.2.2 and 2.3.2 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M21 Small-error dynamics

**Central question.** How does the improvement shrink close to the target?

**Understanding target.** Read the leading quadratic decrease in infidelity after success and the leading linear failure probability. Relate these powers to the shrinking strength of the control.

**Prerequisites.** [M16](#m16-gain-and-replacement-loss), [M19](#m19-scheduling-a-positive-gain), [M20](#m20-a-complete-one-step-example).

**Conceptual connection.** The two rates govern whether charging restarts preserves the inverse-infidelity scaling.

**Sources.** [Sample cost](../science/sample-cost.md). Watrous §1.2.2 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M22 Heralds along a successful attempt

**Central question.** What is fixed by the number of accepted stages?

**Understanding target.** Distinguish the deterministic sequence of accepted overlaps from the random number of raw arrivals. Explain how a failure discards the register and restarts at the source overlap.

**Prerequisites.** [M10](#m10-expectation-with-restarts), [M15](#m15-closure-on-one-scalar), [M19](#m19-scheduling-a-positive-gain), [M21](#m21-small-error-dynamics).

**Conceptual connection.** A single trajectory to the target fidelity describes the output, while many unsuccessful trajectories can contribute to its cost.

**Sources.** [Sample cost](../science/sample-cost.md). Watrous §§1.2.2 and 2.3.2 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M23 Exact renewal accounting

**Central question.** How do failed attempts enter the copy budget?

**Understanding target.** Derive the next-stage expected cost by paying to reach the previous stage, consuming a fresh sample, and restarting with the complementary probability. Include the consumed sample even if it fails.

**Prerequisites.** [M10](#m10-expectation-with-restarts), [M20](#m20-a-complete-one-step-example), [M22](#m22-heralds-along-a-successful-attempt).

**Conceptual connection.** This distinction makes it possible to extract the physical copy count from the numerical trajectory.

**Sources.** [Sample cost](../science/sample-cost.md). Watrous §1.2.2 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M24 The inverse-infidelity cost law

**Central question.** When does the expected copy count grow as the reciprocal of target infidelity?

**Understanding target.** Analyze the scaled expected cost near the target. Identify the positive difference between gain and failure coefficients that yields a finite asymptotic constant.

**Prerequisites.** [M21](#m21-small-error-dynamics), [M22](#m22-heralds-along-a-successful-attempt), [M23](#m23-exact-renewal-accounting).

**Conceptual connection.** The success dynamics alone give the number of accepted stages. The renewal calculation supplies the coefficient that accounts for all discarded inputs.

**Sources.** [Sample cost](../science/sample-cost.md). Watrous §§1.2.1–1.2.2 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M25 Source quality and dimension

**Central question.** Which asymptotic conclusions are uniform in dimension?

**Understanding target.** Distinguish the coefficient for fixed dimension and signal weight from the inverse-infidelity bound for fixed signal weight above one half uniformly over dimension. Connect one retained qudit to its logarithmic encoding size in qubits.

**Prerequisites.** [M12](#m12-the-streaming-task), [M19](#m19-scheduling-a-positive-gain), [M24](#m24-the-inverse-infidelity-cost-law).

**Conceptual connection.** The resulting reduction is in the number of coherent data registers as accuracy increases, with the register dimension explicitly counted.

**Sources.** [Sample cost](../science/sample-cost.md). Watrous §§1.2.2 and 2.1.1–2.1.2 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M26 Output from a classical record

**Central question.** What class of alternative protocols is compared?

**Understanding target.** Identify estimate-and-prepare protocols by how the output is produced from a terminal classical record. Allow collective measurements and a variable stopping time in that class.

**Prerequisites.** [M06](#m06-measurement-effects-and-branches), [M11](#m11-uniform-state-averages), [M12](#m12-the-streaming-task).

**Conceptual connection.** The baseline can use extensive quantum processing before it prepares the output. Its restriction is at the final quantum output.

**Sources.** [Measure-and-prepare benchmark](../science/measure-prepare.md). Watrous §§2.2.3 and 2.3.1–2.3.2 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M27 A bound per measurement record

**Central question.** Why can adaptive stopping still be analyzed?

**Understanding target.** Associate each terminal record with a positive effect on the number of copies it consumed, and apply the symmetric-projector fidelity bound to that record. Use depolarization to transfer the bound from pure-copy inputs to the modeled source.

**Prerequisites.** [M02](#m02-depolarized-input-copies), [M06](#m06-measurement-effects-and-branches), [M11](#m11-uniform-state-averages), [M26](#m26-output-from-a-classical-record).

**Conceptual connection.** The pointwise bound applies even if a record is rare or was selected by a stopping decision.

**Sources.** [Measure-and-prepare benchmark](../science/measure-prepare.md). Watrous §§2.2.3 and 7.2.1–7.2.2 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M28 From records to expected copies

**Central question.** How do different stopping lengths combine into the final bound?

**Understanding target.** Average the record-wise infidelity bound and use convexity of the reciprocal as a function of copy count. Convert a uniform output guarantee into the stated lower bound for expected copies.

**Prerequisites.** [M03](#m03-output-overlap), [M10](#m10-expectation-with-restarts), [M11](#m11-uniform-state-averages), [M27](#m27-a-bound-per-measurement-record).

**Conceptual connection.** The comparison with the streaming procedure uses expected raw-copy counts for the same target overlap.

**Sources.** [Measure-and-prepare benchmark](../science/measure-prepare.md). Watrous §§1.2.1–1.2.2 and 7.2.2 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M29 Finite evidence and physical implementation

**Central question.** What can a finite calculation or an imperfect control establish?

**Understanding target.** Read the verified finite example as an evaluation of the model and recurrence. In the per-stage storage model, relate the square-root infidelity floor to the balance between quadratic gain and linear depolarization loss. Identify the relative strength and storage budgets that preserve inverse-infidelity sample scaling.

**Prerequisites.** [M20](#m20-a-complete-one-step-example), [M21](#m21-small-error-dynamics), [M23](#m23-exact-renewal-accounting), [M25](#m25-source-quality-and-dimension), [M28](#m28-from-records-to-expected-copies).

**Conceptual connection.** The weak gain at high fidelity makes error models consequential. Numerical checks, analytic laws and physical implementations have different evidence requirements.

**Sources.** [Robustness](../science/robustness.md) · [verification guide](../verification/README.md). Watrous §§2.2.1 and 2.3.2 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

### M30 The complete scientific result

**Central question.** How do the coherent branch, the restart law and the comparison fit together?

**Understanding target.** Explain the mechanism from the controlled SWAP through release after the required successful stages. State the source promise, persistent workspace, strongest proved cost regime and exact class of the lower-bound comparison.

**Prerequisites.** [M18](#m18-acceptance-after-sector-measurement), [M19](#m19-scheduling-a-positive-gain), [M24](#m24-the-inverse-infidelity-cost-law), [M25](#m25-source-quality-and-dimension), [M28](#m28-from-records-to-expected-copies), [M29](#m29-finite-evidence-and-physical-implementation).

**Conceptual connection.** The whole account connects a controllable single interaction to a streaming memory reduction and a charged statistical comparison.

**Sources.** [Model](../science/model.md) · [connected scientific account](../science/README.md) · [worked tutorial](TUTORIAL.md). Watrous §§2.1–2.3 and 7.1–7.2 via the [anchor bridge](WATROUS_BRIDGE.md#targeted-reading).

