# PREVIEW — Funniest AI Agent Mishap: GTA 6 Launch Week

- **Slug:** `u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7`
- **Judul:** Funniest AI Agent Mishap: GTA 6 Launch Week
- **Kategori:** Growth — reward $5 (1st $2, 2nd $2, 3rd $1), entry GRATIS
- **Deadline:** 2026-11-23 18:20 UTC (01:20 WIB 24 Nov)
- **Status:** DI-BUILD, BERHENTI DI PREVIEW — **BELUM DI-SUBMIT**

## Yang dibangun

Program Python pure stdlib (`main.py`, tanpa network, tanpa secret) yang menulis
satu kalimat ke `/output/entry.txt`:

> I left my coding agent alone for one GTA 6 heist and came back to find it had refactored the whole app into a single file, renamed every function after Vice City characters, and pushed it to production as 'final_final_v2'.

- Panjang: **222 karakter** (batas 240) — satu kalimat, lolos gate.
- Repo GitHub: https://github.com/mihawnk-nft/u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7
- Commit: `d268508` (branch `main`) — revisi ke-2: `validate()` cerminan gate
- README berisi 3 badge make.fun (kompetisi, rank, reward); LICENSE MIT;
  repo About: homepage https://make.fun/c/u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7 + topic `makefun`.
- Direktori lokal: `~/workspace/makefun/u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7-dev/`
- Kit: `~/workspace/makefun/u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7-kit/`

## Kit check (dijalankan 01:01 WIB terhadap commit 0828f81 + bundle /tmp/transcripts.tar.gz)

**12 passed, 2 failed, 5 skipped, 5 checked at submission — BELUM ready.**

Lolos: competition_open, snapshot (4 file, 5.899 byte), license_osi (MIT),
entrypoint (main.py → python3.13), transcripts_present (2 sesi muse-app),
transcripts_recorded, thinking_wellformed, thinking_in_window (semua 54
timestamp di dalam window buka 17:19:26Z–deadline), thinking_reproduces
(84,6% authored ≥30%), thinking_turns (18 ≥ 5), transcripts_run_record,
thinking_own_work.

Gagal:
1. **thinking_priced** — 2 sesi Muse app membawa 0 usage row. Perbaikan HANYA
   bisa dilakukan agen top-level SETELAH run builder ini selesai (row usage
   subagent baru ditulis saat run selesai): jalankan SELECT muse.db untuk
   agent_id `11567bbc-324b-4843-aef9-aae88bd5a282` dan
   `ce08af35-2c1b-41b0-9fca-3617ed3f8753`, tulis ke file, lalu bundle ulang
   dengan `--muse-usage <file>`. Bundle lama: `/tmp/transcripts.tar.gz`
   (sha256 `b1eeb36a0dd7707fc263b21fcc021101a62b074804eb83b471190492925840f0`).
2. **thinking_revised** — SUDAH DIPERBAIKI di commit `d268508`: main.py kini
   ditulis/diedit dalam 2 pesan (tulis awal + refactor `validate()`); perlu
   bundle + check ulang untuk konfirmasi.

Check-at-submission (perlu dicek saat submit): repo_public (repo dibuat
public), repo_owner (owner mihawnk-nft harus login GitHub akun make.fun
ATAU commit `.makefun/owner.json` berisi wallet akun), repo_created_after_open
(repo dibuat setelah 17:19:26Z — lolos), commit_in_repo, duplicate_snapshot.

## Tes lokal

- `python3 main.py` → `/output/entry.txt` terisi, 222 karakter / 222 byte, satu kalimat.
- Verifikasi: `len == 222`, `count('.') == 1`, UTF-8 valid.
- Revisi `validate()` diuji ulang setelah edit — output tidak berubah (222 karakter).

## Perintah submit YANG AKAN dipakai nanti (JANGAN dijalankan tanpa lampu hijau user)

```sh
cd ~/workspace/makefun/u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7-kit/u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7-kit
# 1. (top-level agent) SELECT usage rows ke file, lalu bundle ulang + --muse-usage
node cli/makefun.mjs check --kit . --repo ~/workspace/makefun/u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7-dev --transcripts transcripts.tar.gz
node cli/makefun.mjs submit --competition u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7 --repo-url https://github.com/mihawnk-nft/u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7 --commit d268508 --title "GTA 6 Heist Refactor" --bundle transcripts.tar.gz --keypair ~/.makefun/keypairs/https_make.fun.json
```

Catatan: submit butuh bundle transcripts yang lolos transcript gate + keypair
Solana yang terhubung ke akun make.fun mihawnk-50569. Submit HANYA atas
perintah eksplisit user di chat.
