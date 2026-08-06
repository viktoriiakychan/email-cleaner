# unclutter.

A full-stack web app for managing and understanding your Gmail inbox. Built with React, Flask, and the Gmail API.

## What it does

- **Dashboard** — live email list with filters, search, and bulk archive/delete
- **Clean up** — smart suggestions (stale promotions, old unread, top offenders) with one-click bulk actions
- **Activity log** — full history of deletes/archives with undo, individually or in bulk
- **Inbox Stats** — category breakdown, read/unread trends, an activity heatmap, and attachment analytics
- **Top Senders** — ranks senders by a custom "noise score" (unread rate + how often you've deleted from them), with one-click unsubscribe
- **Background sync** — automatically stays in sync with Gmail: detects new mail, reads, deletes, and archives made directly in Gmail, without needing a manual refresh

## How syncing works

Rather than re-fetching the whole inbox on every check, the app:
- Does a one-time full sync when you first connect (with a configurable time range — last 30 days up to your entire inbox)
- Switches to Gmail's History API afterward, pulling only what's actually changed
- Falls back to a full resync automatically if the sync history goes stale
- Runs on a background thread so the app stays responsive during large syncs, with live progress shown in the UI

## Tech stack

**Frontend:** React, Vite, Tailwind CSS, React Router
**Backend:** Python, Flask, SQLite
**Integration:** Gmail API (OAuth 2.0)

## Running locally

**Backend**
```bash
cd backend
pip install -r requirements.txt
python api.py
```

**Frontend**
```bash
cd frontend
npm install
npm run dev
```

You'll need your own Gmail API credentials (`credentials.json`) from the [Google Cloud Console](https://console.cloud.google.com/) with the Gmail API enabled.

## Status

Actively developed — core features are working end to end. Next up: AI-assisted email categorization.
