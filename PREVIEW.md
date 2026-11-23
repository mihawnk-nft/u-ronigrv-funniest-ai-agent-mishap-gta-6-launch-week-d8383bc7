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
- Commit: `b510e98` (branch `main`)
- README berisi 3 badge make.fun (kompetisi, rank, reward); LICENSE MIT;
  repo About: homepage https://make.fun/c/u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7 + topic `makefun`.
- Direktori lokal: `~/workspace/makefun/u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7-dev/`
- Kit: `~/workspace/makefun/u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7-kit/`

## Tes lokal

- `python3 main.py` → `/output/entry.txt` terisi, 222 karakter / 222 byte, satu kalimat.
- Verifikasi: `len == 222`, `count('.') == 1`, UTF-8 valid.

## Kit check

- (status menyusul — bundle transcripts sedang dibuat/dicek)

## Perintah submit YANG AKAN dipakai nanti (JANGAN dijalankan tanpa lampu hijau user)

```sh
cd ~/workspace/makefun/u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7-kit/u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7-kit
node cli/makefun.mjs check --kit . --repo ~/workspace/makefun/u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7-dev --transcripts transcripts.tar.gz
node cli/makefun.mjs submit --competition u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7 --repo-url https://github.com/mihawnk-nft/u-ronigrv-funniest-ai-agent-mishap-gta-6-launch-week-d8383bc7 --commit b510e98 --title "GTA 6 Heist Refactor" --bundle transcripts.tar.gz --keypair ~/.makefun/keypairs/https_make.fun.json
```

Catatan: submit butuh bundle transcripts yang lolos transcript gate + keypair
Solana yang terhubung ke akun make.fun mihawnk-50569. Submit HANYA atas
perintah eksplisit user di chat.
