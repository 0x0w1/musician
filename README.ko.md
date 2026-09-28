# musician

[English](README.md) · [설치](#설치) · [사용법](#사용법) · [문서](docs/README.md)

Codex, Claude Code, Antigravity에서 사용하는 Suno 음악 스킬 플러그인입니다.

## 소개

아이디어를 가사, 프롬프트, 제외 요소, 모델별 설정이 포함된 보컬곡 또는 연주곡 작업안으로 구체화합니다. 저장한 프롬프트 수정, 기존 음원의 편집 요청 작성, 전체 스냅샷을 통한 이전 상태 복원을 지원합니다.

v0.3.0은 v6, v6-wild, v6-mini용 작업안과 구형 모델의 기록 재현용 템플릿을 제공합니다. 결과는 사용자가 Suno에 붙여 넣습니다. 플러그인이 음원을 직접 생성하거나 크레딧을 사용하지는 않습니다.

## 설치

**Codex**

```bash
codex plugin marketplace add 0x0w1/musician
codex plugin add suno-music-skills@musician
```

**Claude Code**

```bash
claude plugin marketplace add 0x0w1/musician
claude plugin install suno-music-skills@musician
```

**Antigravity CLI** — 저장소를 내려받은 위치에서 실행합니다.

```bash
agy plugin install ./plugins/suno-music-skills
```

Antigravity IDE/2.0은 플러그인 폴더 설치 도구를 사용합니다. 해당 명령, 로컬 저장소 설치, 업데이트, 필요 환경, 기록 저장 위치는 [설치 안내](docs/installation.md)에 있습니다. 설치 후 새 에이전트 세션을 시작하세요.

## 사용법

자연어로 요청합니다.

```text
다시 시작하는 마음을 한국어 J-Pop으로 만들어줘. 여성 리드 보컬로.
새벽에 독서할 때 들을, 목소리 없는 앰비언트 연주곡을 만들어줘.
기존 Suno 곡에서 첫 번째 후렴의 가사만 바꿔줘.
```

음원을 편집하려면 원본 곡이나 파일을 함께 제공합니다. 작업안은 모든 필드를 다루며, 붙여 넣을 내용과 사용할 수 없거나 확인하지 못한 설정을 구분합니다. 번역은 가사와 따로 제공합니다.

생성 결과를 알려주거나 특정 부분의 변경을 요청할 수 있습니다.

```text
네 번 모두 합창이 들어갔어. 나머지 편곡은 유지해줘.
처음 저장한 버전으로 되돌려줘.
```

## 스킬

| 스킬 | 용도 |
|---|---|
| `suno-vocal-song` | 가사가 있는 노래 |
| `suno-instrumental` | 연주곡과 가사 없는 보컬 질감 |

## 문서

- [문서 안내](docs/README.md)
- [출력 템플릿과 완성 예제](references/output-templates.md)
- [작업 방식과 검증 범위](docs/workflow.md)
- [v0.2.0에서 업데이트](docs/migration.md)

## 라이선스

[Apache-2.0](LICENSE)
