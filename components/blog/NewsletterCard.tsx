'use client';

import { useState } from 'react';

export default function NewsletterCard() {
  const [email, setEmail] = useState('');
  const [subscribed, setSubscribed] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (email) {
      setSubscribed(true);
      setEmail('');
    }
  };

  return (
    <div className="bg-gradient-to-br from-[#0B192C] via-[#1E3A8A] to-[#0B192C] text-white p-8 sm:p-12 rounded-3xl shadow-xl my-12 text-center relative overflow-hidden">
      <div className="max-w-2xl mx-auto relative z-10">
        <span className="inline-block bg-[#DE8017] text-white text-xs font-bold uppercase tracking-wider px-3.5 py-1.5 rounded-full mb-4">
          Stay Informed
        </span>
        <h3 className="text-2xl sm:text-3xl font-extrabold mb-3">
          Get Latest Study Abroad & MBBS Updates
        </h3>
        <p className="text-slate-300 text-sm mb-6 leading-relaxed">
          Join 15,000+ medical aspirants. Receive NMC gazette alerts, university fee updates, and admission deadlines directly in your inbox.
        </p>

        {subscribed ? (
          <div className="bg-emerald-900/60 border border-emerald-500 text-emerald-200 text-sm p-4 rounded-2xl font-semibold">
            ✓ Subscription successful! Welcome to the Atlas Mentor Newsletter.
          </div>
        ) : (
          <form onSubmit={handleSubmit} className="flex flex-col sm:flex-row gap-3 max-w-lg mx-auto">
            <input
              type="email"
              required
              placeholder="Enter your email address..."
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="flex-grow px-5 py-3.5 rounded-xl bg-white/10 border border-white/20 text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-[#DE8017] text-sm"
            />
            <button
              type="submit"
              className="bg-[#DE8017] hover:bg-[#c97112] text-white font-bold text-sm px-6 py-3.5 rounded-xl transition-all shadow-md flex-shrink-0"
            >
              Subscribe Free
            </button>
          </form>
        )}
      </div>
    </div>
  );
}
