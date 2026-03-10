#!/bin/bash

# skill-insight 주간 리뷰 리마인더

# macOS 알림 전송
osascript -e 'display notification "주간 인사이트 리뷰 시간입니다!\n\n터미널에서 실행하세요:\n$ skill-insight review" with title "📋 skill-insight" sound name "Glass"'

# 터미널에도 메시지 (터미널이 열려있다면)
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📋 주간 인사이트 리뷰 시간!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "실행 명령어:"
echo "  $ cd ~/agent-skills/tools/skill-insight"
echo "  $ ./skill-insight.sh scan"
echo "  $ ./skill-insight.sh review"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
