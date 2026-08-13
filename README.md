# Awesome AI Gyms

**The discovery registry for AI gyms — feeding AutoFDE-Lab for selection/planning and GymAct for lawful execution.**

## Upstream acknowledgements & provenance

This project begins with the excellent community curation below. **Please star, cite, and contribute upstream.** We normalize factual metadata and canonical links rather than copying upstream descriptions. Every row in [`registry/gyms.tsv`](registry/gyms.tsv) carries source codes resolved by the exact-commit lock in [`registry/sources.lock.json`](registry/sources.lock.json).

- [Awesome Agent RL Environments](https://github.com/V01dMur10c/awesome-agent-rl-environments) — [4182d60291a0](https://github.com/V01dMur10c/awesome-agent-rl-environments/tree/4182d60291a05fe37a41b55e158ca8cc00845288) — `aarle`
- [Awesome RL Environments](https://github.com/NafiGit/awesome-rl-environments) — [9cddaf098cfb](https://github.com/NafiGit/awesome-rl-environments/tree/9cddaf098cfba1bf66c0c2a78d7c182856d806eb) — `arle`
- [Awesome Agent Benchmarks](https://github.com/RDI-Foundation/awesome-agent-benchmarks) — [1f28ee46bba8](https://github.com/RDI-Foundation/awesome-agent-benchmarks/tree/1f28ee46bba824d5e6895f223b5fc5d86f554ed8) — `aab`
- [RL Environment List](https://github.com/clvrai/awesome-rl-envs) — [08cacf66b2bc](https://github.com/clvrai/awesome-rl-envs/tree/08cacf66b2bc51d07a35043ef74b089f0e9b83f2) — `are`
- [Environments and Simulators for Learning Algorithms](https://github.com/dbobrenko/awesome-ai-environments) — [cbe9f5575b30](https://github.com/dbobrenko/awesome-ai-environments/tree/cbe9f5575b30ecabaea1771e64999b9a5823695e) — `aae`
- [Awesome Gymnasium Data](https://github.com/ishandutta2007/Awesome-Gymnasium-Data) — [04bad480297d](https://github.com/ishandutta2007/Awesome-Gymnasium-Data/tree/04bad480297d8e92200653ce088217dbb432bedb) — `agd`

## DFCM product topology

```text
upstream lists/repos
        │
        ▼
 awesome-ai-gyms
 DISCOVER + PRESERVE
 authority = NONE
        │
        ▼
   AutoFDE-Lab
   SELECT + PLAN
 authority = SELECT_ONLY
        │
        ▼
      GymAct
 ADMIT → MATERIALIZE → OBSERVE → BRCE DO → VERIFY → RECEIPT/REPLAY
```

DFCM rule: preserve the maximum reversible lawful possibility graph before irreversible selection. Catalog membership is **not** installation, compatibility, admission, authority, execution, or proof. Planner compatibility starts `UNKNOWN`; one refused edge narrows topology rather than collapsing the graph.

### Standing

- Registry: `PARTIAL_ALIVE`
- Candidates: **190** across **26** categories
- Candidate default: `UNKNOWN`
- Awesome AI Gyms authority: `NONE`
- AutoFDE-Lab authority from this feed: `SELECT_ONLY`
- Gym execution: GymAct only, after its own admission; no catalog row auto-registers a provider

### Kind coverage

- `benchmark`: 74
- `environment`: 60
- `framework`: 29
- `infrastructure`: 12
- `simulator`: 15

## Machine interface

- [`registry/gyms.tsv`](registry/gyms.tsv) — canonical candidate set.
- [`registry/contract.json`](registry/contract.json) — DFCM/default-standing contract.
- [`schema/awesome-ai-gym.schema.json`](schema/awesome-ai-gym.schema.json) — normalized candidate record schema.
- [`scripts/crawl_upstreams.py`](scripts/crawl_upstreams.py) — exact-pinned DISCOVER crawler; emits a review inbox and never mutates the canonical registry.
- GymAct and AutoFDE-Lab each own a typed adapter over this registry; product semantics are not duplicated here.

Verify: `python scripts/render_readme.py && python scripts/validate_registry.py && python -m unittest discover -s tests -v`.

## Catalog

### Autonomous Driving (4)

[AirSim](https://github.com/Microsoft/AirSim) · [CARLA](https://github.com/carla-simulator/carla) · [HighwayEnv](https://github.com/Farama-Foundation/HighwayEnv) · [MetaDrive](https://github.com/metadriverse/metadrive)

### Coding (13)

[Commit0](https://github.com/commit-0/commit0) · [debug-gym](https://github.com/microsoft/debug-gym) · [LoCoBench-Agent](https://github.com/SalesforceAIResearch/LoCoBench-Agent) · [MLE-bench](https://github.com/openai/mle-bench) · [Multi-SWE-Bench](https://github.com/multi-swe-bench/multi-swe-bench) · [ProjDevBench](https://github.com/zsworld6/projdevbench) · [R2E-Gym](https://github.com/R2E-Gym/R2E-Gym) · [SciCode](https://github.com/scicode-bench/SciCode) · [SWE-bench](https://github.com/SWE-bench/SWE-bench) · [SWE-bench Pro](https://github.com/scaleapi/SWE-bench_Pro-os) · [SWE-bench-Live](https://github.com/microsoft/SWE-bench-Live) · [SWE-Gym](https://github.com/SWE-Gym/SWE-Gym) · [USACO](https://github.com/princeton-nlp/USACO)

### Computer Use (13)

[Agent-S](https://github.com/simular-ai/Agent-S) · [AndroidEnv](https://github.com/google-deepmind/android_env) · [AndroidWorld](https://github.com/google-research/android_world) · [CRAB](https://github.com/camel-ai/crab) · [OSUniverse](https://github.com/agentsea/osuniverse) · [OSWorld](https://github.com/xlang-ai/OSWorld) · [OSWorld-MCP](https://github.com/X-PLUG/OSWorld-MCP) · [SCUBA](https://github.com/SalesforceAIResearch/SCUBA) · [Spider2-V](https://github.com/xlang-ai/Spider2-V) · [Terminal-Bench](https://github.com/laude-institute/terminal-bench) · [Terminal-Bench 2.0](https://github.com/harbor-framework/terminal-bench-2) · [UI-CUBE](https://github.com/UiPath/uipath_enterprise_benchmark) · [Windows Agent Arena](https://github.com/microsoft/WindowsAgentArena)

### Domain Specific (4)

[CityLearn](https://github.com/intelligent-environments-lab/CityLearn) · [FinRL](https://github.com/AI4Finance-Foundation/FinRL) · [Flatland](https://github.com/flatland-association/flatland-rl) · [Gym-ANM](https://github.com/robinhenry/gym-anm)

### Embodied (3)

[BEHAVIOR-1K](https://github.com/StanfordVL/BEHAVIOR-1K) · [MineAnyBuild](https://github.com/MineAnyBuild/MineAnyBuild) · [Robotouille](https://github.com/portal-cornell/robotouille)

### Enterprise (1)

[CRMArena](https://github.com/SalesforceAIResearch/CRMArena)

### Games (18)

[Arcade Learning Environment](https://github.com/Farama-Foundation/Arcade-Learning-Environment) · [BALROG](https://github.com/balrog-ai/BALROG) · [Bomberland](https://github.com/coderonehq/bomberland) · [CoinRun](https://github.com/openai/coinrun) · [Craftax](https://github.com/MichaelTMatthews/Craftax) · [Crafter](https://github.com/danijar/crafter) · [Google Research Football](https://github.com/google-research/football) · [Griddly](https://github.com/Bam4d/Griddly) · [Gym Retro](https://github.com/openai/retro) · [MineDojo](https://github.com/MineDojo/MineDojo) · [MineRL](https://github.com/minerllabs/minerl) · [MiniHack](https://github.com/facebookresearch/minihack) · [NetHack Learning Environment](https://github.com/heiner/nle) · [Procgen Benchmark](https://github.com/openai/procgen) · [Pycolab](https://github.com/deepmind/pycolab) · [PySC2](https://github.com/google-deepmind/pysc2) · [Stable-Retro](https://github.com/Farama-Foundation/stable-retro) · [Voyager](https://github.com/MineDojo/Voyager)

### General Agent (16)

[AgencyBench](https://github.com/GAIR-NLP/AgencyBench) · [AgentBench](https://github.com/THUDM/AgentBench) · [AgentGym](https://github.com/WooooDyy/AgentGym) · [AgentGym-RL](https://github.com/WooooDyy/AgentGym-RL) · [GEM](https://github.com/axon-rl/gem) · [HCAST](https://github.com/METR/hcast-public) · [Meta Agents Research Environments](https://github.com/facebookresearch/meta-agents-research-environments) · [OpenAI Universe](https://github.com/openai/universe) · [OpenPipe ART](https://github.com/OpenPipe/ART) · [prime-rl](https://github.com/PrimeIntellect-ai/prime-rl) · [RAGEN](https://github.com/RAGEN-AI/RAGEN) · [SkyRL](https://github.com/NovaSky-AI/SkyRL) · [UltraHorizon](https://github.com/StarDewXXX/UltraHorizon) · [VAGEN](https://github.com/RAGEN-AI/VAGEN) · [verifiers](https://github.com/PrimeIntellect-ai/verifiers) · [verl-agent](https://github.com/langfengQ/verl-agent)

### High Throughput (4)

[Brax](https://github.com/google/brax) · [Gymnax](https://github.com/RobertTLange/gymnax) · [JaxMARL](https://github.com/FLAIROx/JaxMARL) · [Jumanji](https://github.com/instadeep/jumanji)

### Infrastructure (11)

[Acme](https://github.com/google-deepmind/acme) · [CleanRL](https://github.com/vwxyzjn/cleanrl) · [EnvPool](https://github.com/sail-sg/envpool) · [Minari](https://github.com/Farama-Foundation/Minari) · [OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) · [Rliable](https://github.com/google-research/rliable) · [RLlib](https://github.com/ray-project/ray/tree/master/rllib) · [Sample Factory](https://github.com/alex-petrenko/sample-factory) · [SB3 Zoo](https://github.com/DLR-RM/rl-baselines3-zoo) · [Stable Baselines3](https://github.com/DLR-RM/stable-baselines3) · [Tianshou](https://github.com/thu-ml/tianshou)

### Memory (3)

[LoCoMo](https://github.com/snap-research/locomo) · [LoCoMo-Plus](https://github.com/xjtuleeyf/Locomo-Plus) · [LongMemEval](https://github.com/xiaowu0162/LongMemEval)

### Multi Agent (6)

[Melting Pot](https://github.com/google-deepmind/meltingpot) · [Neural MMO](https://github.com/NeuralMMO/environment) · [Overcooked-AI](https://github.com/HumanCompatibleAI/overcooked_ai) · [PommerMan](https://github.com/MultiAgentLearning/playground) · [SMACv2](https://github.com/oxwhirl/smacv2) · [VMAS](https://github.com/proroklab/VectorizedMultiAgentSimulator)

### Navigation (9)

[AI2-THOR](https://github.com/allenai/ai2thor) · [DeepMind Lab](https://github.com/deepmind/lab) · [GibsonEnv](https://github.com/StanfordVL/GibsonEnv) · [Gym-Maze](https://github.com/zuoxingdong/gym-maze) · [HoME Platform](https://github.com/HoME-Platform/home-platform) · [House3D](https://github.com/facebookresearch/House3D) · [MINOS](https://github.com/minosworld/minos) · [Project Malmo](https://github.com/Microsoft/malmo) · [VizDoom](https://github.com/mwydmuch/ViZDoom)

### Planning (1)

[REALM-Bench](https://github.com/genglongling/REALM-Bench)

### Reasoning Games (1)

[MiniGrid](https://github.com/Farama-Foundation/Minigrid)

### Reasoning Text (5)

[ALFWorld](https://github.com/alfworld/alfworld) · [Reasoning Gym](https://github.com/open-thought/reasoning-gym) · [ScienceWorld](https://github.com/allenai/ScienceWorld) · [TextArena](https://github.com/LeonGuertler/TextArena) · [TextWorld](https://github.com/microsoft/TextWorld)

### Research (9)

[AstaBench](https://github.com/allenai/asta-bench) · [BrowseComp-Plus](https://github.com/texttron/BrowseComp-Plus) · [DeepResearch Bench](https://github.com/Ayanami0730/deep_research_bench) · [DeepScholar-Bench](https://github.com/guestrin-lab/deepscholar-bench) · [InnovatorBench](https://github.com/GAIR-NLP/InnovatorBench) · [MMDeepResearch-Bench](https://github.com/AIoT-MLSys-Lab/MMDeepResearch-Bench) · [PaperArena](https://github.com/Melmaphother/PaperArena) · [RE-Bench](https://github.com/METR/RE-Bench) · [WideSearch](https://github.com/ByteDance-Seed/WideSearch)

### Robotics (16)

[Assistive-gym](https://github.com/Healthcare-Robotics/assistive-gym) · [CALVIN](https://github.com/mees/calvin) · [Dexterous Gym](https://github.com/henrycharlesworth/dexterous-gym) · [DoorGym](https://github.com/PSVL/DoorGym) · [Gym Gazebo 2](https://github.com/AcutronicRobotics/gym-gazebo2) · [Gym Ignition](https://github.com/robotology/gym-ignition) · [Gymnasium-Robotics](https://github.com/Farama-Foundation/Gymnasium-Robotics) · [Habitat Lab](https://github.com/facebookresearch/habitat-lab) · [Isaac Lab](https://github.com/isaac-sim/IsaacLab) · [ManiSkill](https://github.com/haosulab/ManiSkill) · [Meta-World](https://github.com/Farama-Foundation/Metaworld) · [MuJoCo](https://github.com/google-deepmind/mujoco) · [RAISIM](https://github.com/leggedrobotics/raisimLib) · [Rex-Gym](https://github.com/nicrusso7/rex-gym) · [Roboschool](https://github.com/openai/roboschool) · [robosuite](https://github.com/ARISE-Initiative/robosuite)

### Robotics Control (1)

[DeepMind Control Suite](https://github.com/google-deepmind/dm_control)

### Safety (6)

[Agent-SafetyBench](https://github.com/thu-coai/Agent-SafetyBench) · [AgentAuditor](https://github.com/Astarojth/AgentAuditor) · [MCP-SafetyBench](https://github.com/xjzzzzzzzz/MCPSafety) · [MT-AgentRisk / ToolShield](https://github.com/CHATS-lab/ToolShield) · [OpenAgentSafety](https://github.com/sani903/OpenAgentSafety) · [OS-Harm](https://github.com/tml-epfl/os-harm)

### Security (8)

[Agent Security Bench](https://github.com/agiresearch/ASB) · [CAIBench](https://github.com/aliasrobotics/cai/tree/main/benchmarks) · [CVE-Bench](https://github.com/uiuc-kang-lab/cve-bench) · [CyberGym](https://github.com/sunblaze-ucb/cybergym) · [DoomArena](https://github.com/ServiceNow/DoomArena) · [ExCyTIn-Bench / SecRL](https://github.com/microsoft/SecRL) · [SEC-bench](https://github.com/SEC-bench/SEC-bench) · [WASP](https://github.com/facebookresearch/wasp)

### Simulation (1)

[Unity ML-Agents](https://github.com/Unity-Technologies/ml-agents)

### Standards (5)

[Gymnasium](https://github.com/Farama-Foundation/Gymnasium) · [OpenAI Gym](https://github.com/openai/gym) · [OpenEnv](https://github.com/meta-pytorch/OpenEnv) · [PettingZoo](https://github.com/Farama-Foundation/PettingZoo) · [Shimmy](https://github.com/Farama-Foundation/Shimmy)

### Strategy Games (4)

[OpenSpiel](https://github.com/google-deepmind/open_spiel) · [Pgx](https://github.com/sotetsuk/pgx) · [RLCard](https://github.com/datamllab/rlcard) · [TorchCraft](https://github.com/TorchCraft/TorchCraft)

### Tool Use (12)

[API-Bank](https://github.com/AlibabaResearch/DAMO-ConvAI/tree/main/api-bank) · [AppWorld](https://github.com/StonyBrookNLP/appworld) · [Gorilla / APIBench](https://github.com/ShishirPatil/gorilla) · [GTA](https://github.com/open-compass/GTA) · [MCP-Bench](https://github.com/Accenture/mcp-bench) · [MCP-Universe](https://github.com/SalesforceAIResearch/MCP-Universe) · [tau-bench](https://github.com/sierra-research/tau-bench) · [tau2-bench](https://github.com/sierra-research/tau2-bench) · [Tool Decathlon](https://github.com/hkust-nlp/Toolathlon) · [ToolBench](https://github.com/OpenBMB/ToolBench) · [ToolComp](https://github.com/vaskar-nath/toolcomp) · [ToolSandbox](https://github.com/apple/ToolSandbox)

### Web (16)

[AgentLab](https://github.com/ServiceNow/AgentLab) · [AssistantBench](https://github.com/oriyor/assistantbench) · [BrowseComp](https://github.com/openai/simple-evals) · [BrowserArena](https://github.com/sagnikanupam/browserarena) · [BrowserGym](https://github.com/ServiceNow/BrowserGym) · [Mind2Web](https://github.com/OSU-NLP-Group/Mind2Web) · [Mind2Web 2](https://github.com/OSU-NLP-Group/Mind2Web-2) · [Online-Mind2Web](https://github.com/OSU-NLP-Group/Online-Mind2Web) · [VisualWebArena](https://github.com/web-arena-x/visualwebarena) · [WebArena](https://github.com/web-arena-x/webarena) · [WebArena-Infinity](https://github.com/web-arena-x/webarena-infinity) · [WebArena-Verified](https://github.com/ServiceNow/webarena-verified) · [WebChoreArena](https://github.com/WebChoreArena/WebChoreArena) · [WebRL](https://github.com/THUDM/WebRL) · [WebShop](https://github.com/princeton-nlp/WebShop) · [WorkArena](https://github.com/ServiceNow/WorkArena)

## Contribution law

Increase the reversible lawful graph without manufacturing standing. Preserve provenance; keep unknowns unknown; do not mark a gym ALIVE from documentation, importability, CI metadata, popularity, or an upstream benchmark claim. See [CONTRIBUTING.md](CONTRIBUTING.md).
