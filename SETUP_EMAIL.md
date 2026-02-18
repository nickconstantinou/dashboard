# Setting Up Griptide Email

## Quick Setup (5 min)

### Option A: Gmail (Easiest)

1. **Create new Gmail**: https://gmail.com (or use existing)
2. **Share access**: Give me the credentials via 1Password

### Option B: Custom Domain (More Professional)

If you own `nickconstantinou.co.uk`:

1. **Create email alias** in your domain provider:
   - `griptide@nickconstantinou.co.uk` → forwards to your main email
   
2. **Or use Cloudflare Email Routing** (free):
   - Go to Cloudflare Dashboard → your domain
   - Email Routing → Create rule
   - Destination: your main email

3. **Give me SMTP access** to send from this address:
   - App password (Gmail): https://myaccount.google.com/apppasswords
   - Or store in 1Password

---

## What I'll Need

Once set up, store in 1Password:

```
Email: griptide@...
SMTP Host: smtp.gmail.com
SMTP Port: 587
Username: your-email@gmail.com
App Password: xxxx xxxx xxxx xxxx
```

---

## What I Can Do With Email Access

- ✅ Sign up for services (PostHog, etc.)
- ✅ Read notifications/digests you forward
- ✅ Send invites confirmations
- ✅ Help with account management
- ❌ Never access your main inbox without permission

---

## Alternative: Just Forward Me Links

For now, just forward/paste invites to me in Telegram. That's secure and simplest.
