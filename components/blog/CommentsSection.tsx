'use client';

import { useState } from 'react';

interface Comment {
  id: string;
  name: string;
  date: string;
  text: string;
  avatar?: string;
}

export default function CommentsSection() {
  const [comments, setComments] = useState<Comment[]>([
    {
      id: '1',
      name: 'Aakash Verma',
      date: 'July 26, 2026',
      text: 'Extremely detailed article! Cleared all my doubts regarding NMC 2021 gazette regulations for Georgia. Thank you Atlas Mentor!',
    },
    {
      id: '2',
      name: 'Dr. Sneha Reddy',
      date: 'July 24, 2026',
      text: 'Great breakdown of FMGE / NExT preparation strategy. The comparison table of living expenses in Russia vs Uzbekistan is very helpful for parents.',
    },
  ]);

  const [form, setForm] = useState({ name: '', email: '', text: '' });
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (form.name && form.text) {
      const newComment: Comment = {
        id: Date.now().toString(),
        name: form.name,
        date: 'Just now',
        text: form.text,
      };
      setComments([newComment, ...comments]);
      setForm({ name: '', email: '', text: '' });
      setSubmitted(true);
      setTimeout(() => setSubmitted(false), 3000);
    }
  };

  return (
    <section className="bg-white p-6 sm:p-8 rounded-3xl border border-slate-200/90 shadow-sm my-12">
      <h3 className="text-xl font-extrabold text-[#0B192C] mb-6 flex items-center space-x-2">
        <span>Comments ({comments.length})</span>
      </h3>

      {/* Comment Form */}
      <div className="bg-slate-50 p-6 rounded-2xl border border-slate-200/80 mb-8">
        <h4 className="text-sm font-bold text-[#0B192C] mb-3">Leave a Reply</h4>
        {submitted && (
          <div className="bg-emerald-100 text-emerald-800 text-xs p-3 rounded-xl mb-4 font-medium">
            ✓ Your comment has been posted successfully!
          </div>
        )}
        <form onSubmit={handleSubmit} className="space-y-4">
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label className="block text-xs font-semibold text-slate-600 mb-1">Your Name *</label>
              <input
                type="text"
                required
                placeholder="e.g. Rahul Sharma"
                value={form.name}
                onChange={(e) => setForm({ ...form, name: e.target.value })}
                className="w-full px-3.5 py-2.5 text-xs bg-white border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#DE8017]"
              />
            </div>
            <div>
              <label className="block text-xs font-semibold text-slate-600 mb-1">Email Address *</label>
              <input
                type="email"
                required
                placeholder="e.g. rahul@gmail.com"
                value={form.email}
                onChange={(e) => setForm({ ...form, email: e.target.value })}
                className="w-full px-3.5 py-2.5 text-xs bg-white border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#DE8017]"
              />
            </div>
          </div>
          <div>
            <label className="block text-xs font-semibold text-slate-600 mb-1">Comment *</label>
            <textarea
              rows={4}
              required
              placeholder="Write your thoughts or questions..."
              value={form.text}
              onChange={(e) => setForm({ ...form, text: e.target.value })}
              className="w-full px-3.5 py-2.5 text-xs bg-white border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-[#DE8017]"
            />
          </div>
          <button
            type="submit"
            className="bg-[#0B192C] hover:bg-[#DE8017] text-white text-xs font-bold px-6 py-2.5 rounded-xl transition-all duration-300 shadow-md"
          >
            Post Comment
          </button>
        </form>
      </div>

      {/* List of Comments */}
      <div className="space-y-4">
        {comments.map((comment) => (
          <div key={comment.id} className="p-4 rounded-2xl border border-slate-100 bg-white space-y-2">
            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-2.5">
                <div className="w-8 h-8 rounded-full bg-[#DE8017] text-white font-bold text-xs flex items-center justify-center">
                  {comment.name.charAt(0)}
                </div>
                <span className="text-sm font-bold text-[#0B192C]">{comment.name}</span>
              </div>
              <span className="text-[11px] text-slate-400">{comment.date}</span>
            </div>
            <p className="text-slate-600 text-xs sm:text-sm pl-10 leading-relaxed">{comment.text}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
